from django.contrib import admin
from .models import Faq, HomeCarouselImage, SocialMedia, ContactInformation, Banner
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import mark_safe, format_html
from abstractapp.admin import BaseModelAdmin


# Register your models here.

@admin.register(HomeCarouselImage)
class HomeCarouselImageAdmin(SortableAdminMixin,BaseModelAdmin):
    # list_display = [field.name for field in HomeCarouselImage._meta.get_fields()]
    # list_display_links = list_display
    ordering = 'custom_order',
    readonly_fields = ('image_preview',)

    def image_preview(self,obj):
        return format_html('<img src="{}"  height="150" />', obj.image.url)

    @property
    def list_display(self):
        return [field.name for field in self.model._meta.get_fields() if field.name != 'image']+['image_preview']

@admin.register(ContactInformation)
class ContactInformationAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ['name','info','link','is_active','is_featured']
    list_editable = ('is_active','is_featured')
    # list_display_links = [x for x in list_display if x not in ('is_active','is_featured')]
    ordering = 'custom_order',
    readonly_fields = 'link',

    @property
    def list_display_links(self):
        return [x for x in self.list_display if x not in self.list_editable]


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


@admin.register(Banner)
class HomePageAdmin(SortableAdminMixin, BaseModelAdmin):
    ordering = ('custom_order',)

    def image_preview(self, obj):
        return mark_safe('<img src="{}" height="150" />'.format(obj.image.url))

    readonly_fields = ['image_preview']
    

    @property
    def list_display(self):
        return [field.name for field in self.model._meta.get_fields() if field.name != 'image']+['image_preview']
    #     # model_name = self.model.__name__  # 这里获取模型的类名，即 "HomePage" 这里，self.model指向HomePage，因此self.model.__name__会返回字符串"HomePage"。

    
    # @property
    # def list_display_links(self):
    #     return [x for x in self.list_display if x not in self.list_editable]