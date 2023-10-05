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
    list_display = ['name','info','link']
    list_display_links = list_display
    ordering = 'custom_order',
    readonly_fields = 'link',

    def save_model(self, request, obj, form, change):
        # 使用link_template的值渲染rendered_link
        if obj.link_template:
            obj.link = obj.link_template.replace("{{contact_info}}", obj.info)
        else:
            obj.link = None
        super().save_model(request, obj, form, change)

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
