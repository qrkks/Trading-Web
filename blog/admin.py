from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html
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
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','custom_order','slug','category','created_at','updated_at']
    list_display_links = [x for x in list_display if x not in ['custom_order']]
    readonly_fields = ['image_preview']

    def image_preview(self,obj):
        return format_html('<img src="{}" height="150" ',obj.image.url)