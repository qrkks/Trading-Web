from django.contrib import admin
from .models import Category, Product, ProductImage
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.utils.html import mark_safe
from adminsortable2.admin import SortableAdminMixin

# Register your models here.

######################### 产品分类模型管理 ##############################
# 自定义管理类
@admin.register(Category)
class CategoryModelAdmin(DraggableMPTTAdmin):
    list_display = [
        'tree_actions',
        'indented_title',
        # ...more fields if needed...
        'parent', 'slug', 'level', 'custom_order'
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

@admin.register(Product)
# class ProductModelAdmin(SortableAdminMixin,admin.ModelAdmin):
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields() if field.name != 'images']
    # list_display = ['id','name','category','is_active']
    list_display_links = [x for x in list_display if x not in ['is_active','is_featured','custom_order']]
    list_editable = ['is_active','is_featured','custom_order']  # 允许编辑的字段
    search_fields = ['name','slug']
    # prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageAdmin]
    ordering = ['custom_order']

