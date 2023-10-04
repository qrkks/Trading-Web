from django.contrib import admin

# Register your models here.
from .models import Inquiry, NotificationInbox

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'institution', 'email', 'phone', 'country_region', 'state', 'city', 'message',  'source_ip', 'country_from_ip','created_at','source_webpage',]
    list_display_links = list_display
    readonly_fields = ('created_at',)

@admin.register(NotificationInbox)
class NotificationInboxAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NotificationInbox._meta.fields]
    list_display_links = list_display

