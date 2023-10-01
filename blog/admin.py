from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from adminsortable2.admin import SortableAdminMixin
from .models import Category, Blog

# Register your models here.

@admin.register(Category)
class BlogCategoryAdmin(DraggableMPTTAdmin):
    list_display = [
        'tree_actions',
        'indented_title',
        # ...more fields if needed...
        'parent', 'slug', 'level', 'custom_order'
    ]
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Blog)
class BlogAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ['title','custom_order','slug','category']
    list_display_links = [x for x in list_display if x not in ['custom_order']]
    ordering = ['custom_order']