from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
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
    pass