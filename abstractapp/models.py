from django.db import models, transaction
from django.utils import timezone
from slugify import slugify

from abstractapp.manager import CommonManager

# Create your models here.

# 抽象模型


class BaseModel(models.Model):
    custom_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    objects = CommonManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # 如果是新记录，并且没有指定排序值
        if not self.pk and self.custom_order == 0:
            with transaction.atomic():
                max_custom_order = self.__class__.objects.aggregate(models.Max('custom_order'))[
                    'custom_order__max'] or 0
                self.custom_order = max_custom_order + 1
        super().save(*args, **kwargs)


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
