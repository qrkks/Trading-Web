from django.contrib import admin
from .models import Category, Product
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin


# Register your models here.
# @admin.register(Category)
# class CategoryAdmin(MPTTModelAdmin):
#     list_display = ('name', 'parent', 'level','custom_order')


# admin.site.register(Category, MPTTModelAdmin)

# 自定义管理类
class CategoryModelAdmin(DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
        # ...more fields if needed...
        'parent', 'slug', 'level', 'custom_order'
    )
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('name',)}


# 注册模型和自定义管理类
admin.site.register(Category, CategoryModelAdmin)


class ProductModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields()]
    list_display_links = list_display
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product,ProductModelAdmin)
