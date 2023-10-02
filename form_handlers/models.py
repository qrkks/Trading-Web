from django.db import models

# Create your models here.


class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    country_region = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    message = models.TextField()
    source_webpage = models.URLField(blank=True)
    source_ip = models.GenericIPAddressField(blank=True,null=True)
    country_from_ip = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'inquiries'
