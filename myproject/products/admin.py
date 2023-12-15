from .models import ProductImage
from import_export import resources
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
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


# Register your models here.

######################### 产品分类模型管理 ##############################
# 自定义管理类
@admin.register(Category)
class ProductCategoryModelAdmin(DraggableMPTTAdmin):
    list_display = [
        'tree_actions',
        'indented_title',
        # ...more fields if needed...
        'id', 'code', 'parent', 'slug', 'level', 
    ]
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('name',)}


####################### 产品图片模型管理 ########################

class ProductImageInlineAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1  # 显示一个额外的空行，以便批量上传多个图片
    fields = ['image', 'is_for_display', 'image_preview', 'image_size_kb']  # 明确指定要显示的字段

    def image_preview(self, obj):
        return mark_safe('<img src="{}"  height="150" />'.format(obj.image.url))

    readonly_fields = ['image_preview', 'image_size_kb']


# admin.site.register(ProductImage)


class ProductImageResource(resources.ModelResource):
    class Meta:
        model = ProductImage
        # 指定要导入的字段
        fields = ('id', 'image', 'product')
        # 或者使用 exclude 来排除一些字段
        # exclude = ('id',)

# Register the ProductImage model with the admin site
@admin.register(ProductImage)
class ProductImageImportExportAdmin(ImportExportModelAdmin):
    # Set the resource class to use for importing and exporting data
    resource_class = ProductImageResource
    
    # Define a method to display a preview of the image in the admin list view
    def image_preview(self, obj):
        # Check if the object has an image associated with it
        if obj.image:
            # If it does, generate an HTML tag to display the image
            return mark_safe(f'<img src="{obj.image.url}" height="150" />')
        # If there is no image, return an empty string
        return ""
    
    # Set the readonly fields that should be displayed in the admin detail view
    readonly_fields = ['image_preview',]
    
    # Set the fields that should be displayed in the admin list view
    list_display = ['id', 'product', 'image_preview']

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
class ProductModelAdmin(ImportExportModelAdmin, SortableAdminMixin):
    # class ProductModelAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Product._meta.get_fields() if  is_displayable_field(field)]
    # list_display = [field.name for field in Product._meta.get_fields() if field.name not in ['images','related_products','product','tags','TaggableManager','_TaggableManager'] ]
    list_display = ['id', 'name','code', 'slug', 'category', 'custom_order',
                    'is_active', 'is_featured', 'created_at', 'updated_at']
    list_display_links = [x for x in list_display if x not in [
        'is_active', 'is_featured', 'custom_order']]
    # prepopulated_fields = {'slug': ('name',)}
    # list_display_links = 'name',
    list_editable = ['custom_order', 'is_active', 'is_featured',]  # 允许编辑的字段
    search_fields = ['name', 'slug',]
    inlines = [ProductImageInlineAdmin]
    ordering = ['-custom_order', '-is_active', '-is_featured']
    list_filter = (CategoryFilter,)  # 允许通过类别过滤
    filter_horizontal = 'related_products',
