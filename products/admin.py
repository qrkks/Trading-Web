from django.contrib import admin
from .models import Category, Product, ProductImage
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.utils.html import mark_safe


# Register your models here.
# @admin.register(Category)
# class CategoryAdmin(MPTTModelAdmin):
#     list_display = ('name', 'parent', 'level','custom_order')


# admin.site.register(Category, MPTTModelAdmin)

######################### 产品分类模型管理 ##############################
# 自定义管理类
class CategoryModelAdmin(DraggableMPTTAdmin):
    list_display = [
        'tree_actions',
        'indented_title',
        # ...more fields if needed...
        'parent', 'slug', 'level', 'custom_order'
    ]
    # list_display += [field.name for field in Category._meta.get_fields() if field.name not in ('parent','products')]
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('name',)}


# 注册模型和自定义管理类
admin.site.register(Category, CategoryModelAdmin)


####################### 产品图片模型管理 ########################

def delete_selected_product_images(modeladmin, request, queryset):
    for image in queryset:
        # 执行删除操作
        image.delete()

delete_selected_product_images.short_description = "Delete selected product images"

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1  # 显示一个额外的空行，以便批量上传多个图片

    def image_preview(self, obj):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(obj.image.url))

    readonly_fields = ['image_preview']
    actions = [delete_selected_product_images]
    
admin.site.register(ProductImage)

##################### 产品模型管理 ###################################
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields() if field.name != 'images']
    # list_display = ['id','name','category','is_active']
    list_display_links = [x for x in list_display if x !='is_active']
    list_editable = ['is_active']  # 允许编辑的字段
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageAdmin]


admin.site.register(Product,ProductModelAdmin)
