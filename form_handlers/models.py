from django.db import models

# Create your models here.


class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15,blank=True,null=True)
    country_region = models.CharField(max_length=100)
    state = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    message = models.TextField()
    source_webpage = models.URLField(blank=True,null=True)
    source_ip = models.GenericIPAddressField(blank=True,null=True)
    country_from_ip = models.CharField(max_length=100, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True,editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'inquiries'

class NotificationInbox(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        verbose_name_plural = 'notification inboxes'
        
    def __str__(self) -> str:
        return self.email
    