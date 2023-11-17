from django.db import models

# Create your models here.
class ViewCount(models.Model):
    counts = models.IntegerField(default=0)
    