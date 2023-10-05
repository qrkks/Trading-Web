from django.contrib import admin
from .models import Faq, HomeCarouselImage, SocialMedia, ContactInformation
from adminsortable2.admin import SortableAdminMixin

# Register your models here.

@admin.register(HomeCarouselImage)
class HomeCarouselImageAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = [field.name for field in HomeCarouselImage._meta.get_fields()]
    list_display_links = list_display
    ordering = 'custom_order',

@admin.register(ContactInformation)
class ContactInformationAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ['name','info']
    list_display_links = list_display
    ordering = 'custom_order',

@admin.register(SocialMedia)
class SocialMediaAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ['name','link']
    list_display_links = list_display
    ordering = 'custom_order',

@admin.register(Faq)
class FaqAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ['question','answer']
    list_display_links = list_display
    ordering = ['custom_order']
