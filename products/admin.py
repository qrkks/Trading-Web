from django.utils.translation import gettext_lazy as _
from django.db.models.fields.reverse_related import ManyToOneRel, ManyToManyRel
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
from django.db.models.fields.related_descriptors import ReverseManyToOneDescriptor
from django.contrib import admin
from .models import Category, Product, ProductImage
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.utils.html import mark_safe
from adminsortable2.admin import SortableAdminMixin
from django.db import models
from taggit.managers import TaggableManager


# Register your models here.

######################### 产品分类模型管理 ##############################
# 自定义管理类
@admin.register(Category)
class ProductCategoryModelAdmin(DraggableMPTTAdmin):
    list_display = [
        'tree_actions',
        'indented_title',
        # ...more fields if needed...
        'id', 'parent', 'slug', 'level', 'custom_order'
    ]
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('name',)}


####################### 产品图片模型管理 ########################

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1  # 显示一个额外的空行，以便批量上传多个图片

    def image_preview(self, obj):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(obj.image.url))

    readonly_fields = ['image_preview']


admin.site.register(ProductImage)

##################### 产品模型管理 ###################################


def is_displayable_field(field):
    # Exclude many-to-many fields
    if isinstance(field, (ManyToManyField, ManyToManyRel)):
        return False

    # Exclude reverse relation fields
    if isinstance(field, ManyToOneRel):
        return False

    # Exclude TaggableManager from taggit
    if isinstance(field, TaggableManager):
        return False

    # Exclude other non-displayable fields
    # ...

    # If none of the above conditions are met, the field is displayable
    return True


class CategoryFilter(admin.SimpleListFilter):
    title = _('category')  # Human-readable title
    parameter_name = 'category'  # URL query parameter

    def lookups(self, request, model_admin):
        # You might want to customize this to display categories in a hierarchical manner
        return [(c.id, c.name) for c in Category.objects.all()]

    def queryset(self, request, queryset):
        # Filtering logic here
        if self.value():
            category = Category.objects.get(id=self.value())
            sub_categories = category.get_descendants(include_self=True)
            return queryset.filter(category__in=sub_categories)
        return queryset


@admin.register(Product)
class ProductModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    # class ProductModelAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Product._meta.get_fields() if  is_displayable_field(field)]
    # list_display = [field.name for field in Product._meta.get_fields() if field.name not in ['images','related_products','product','tags','TaggableManager','_TaggableManager'] ]
    list_display = ['id', 'name', 'slug', 'category',
                    'is_active', 'is_featured', 'created_at', 'updated_at']
    list_display_links = [x for x in list_display if x not in [
        'is_active', 'is_featured', 'custom_order']]
    # prepopulated_fields = {'slug': ('name',)}
    # list_display_links = 'name',
    list_editable = ['is_active', 'is_featured',]  # 允许编辑的字段
    search_fields = ['name', 'slug',]
    inlines = [ProductImageAdmin]
    ordering = ['custom_order', '-is_active', '-is_featured']
    list_filter = (CategoryFilter,)  # 允许通过类别过滤
