from django.db import models

from .manager import CommonManager
from .func import generate_slug, generate_custom_order

# Create your models here.

# 抽象模型


class BaseModel(models.Model):
    custom_order = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    objects = CommonManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        generate_custom_order(self, *args, **kwargs)
        super().save(*args, **kwargs)


# Mixin类
class SlugMixin(models.Model):
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        generate_slug(self, *args, **kwargs)
        super().save(*args, **kwargs)


class SeoMixin(models.Model):
    # 页面SEO信息
    page_title = models.CharField(max_length=100, null=True, blank=True)
    page_keywords = models.CharField(max_length=100, null=True, blank=True)
    page_description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
