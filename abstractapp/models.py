from django.db import models
from django.utils import timezone
from slugify import slugify

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
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            manager = getattr(self.__class__, self._meta.default_manager_name)
            while manager.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

class SeoMixin(models.Model):
    # 页面SEO信息
    page_title = models.CharField(max_length=100, null=True, blank=True)
    page_keywords = models.CharField(max_length=100, null=True, blank=True)
    page_description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
