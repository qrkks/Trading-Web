from django.contrib import admin

from .models import Inquiry, NotificationInbox
from abstractapp.admin import BaseModelAdmin
# Register your models here.

@admin.register(Inquiry)
class InquiryAdmin(BaseModelAdmin):
    list_display = ['name', 'institution', 'email', 'phone', 'country_region', 'state', 'city', 'message',  'source_ip', 'country_from_ip','created_at','source_webpage',]
    list_display_links = list_display
    readonly_fields = ('created_at',)
    list_editable = []

@admin.register(NotificationInbox)
class NotificationInboxAdmin(BaseModelAdmin):
    # list_display = [f.name for f in NotificationInbox._meta.fields]
    # list_display_links = list_display
    pass
