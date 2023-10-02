from django.contrib import admin

# Register your models here.
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'institution', 'email', 'phone', 'country_region', 'state', 'city', 'message', 'source_webpage', 'source_ip', 'country_from_ip']
