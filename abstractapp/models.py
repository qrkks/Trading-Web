from django.db import models
from django.utils import timezone

# Create your models here.

# 抽象模型
class BaseModel(models.Model):
    custom_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        abstract = True

# Mixin类
class SlugMixin(models.Model):
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        abstract = True

