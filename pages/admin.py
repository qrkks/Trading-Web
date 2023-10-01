from django.contrib import admin
from .models import HomeCarouselImage
from adminsortable2.admin import SortableAdminMixin

# Register your models here.

@admin.register(HomeCarouselImage)
class HomeCarouselImageAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = [field.name for field in HomeCarouselImage._meta.get_fields()]
    list_display_links = list_display
    ordering = 'custom_order',