from django.contrib import admin
from .models import Category
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin


# Register your models here.
# @admin.register(Category)
# class CategoryAdmin(MPTTModelAdmin):
#     list_display = ('name', 'parent', 'level','custom_order')


# admin.site.register(Category, MPTTModelAdmin)

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
        'parent','slug', 'level', 'custom_order'
    ),
    list_display_links=(
        'indented_title',
    ),
)
