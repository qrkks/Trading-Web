from django.db import models

# Create your models here.

# 抽象模型
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Mixin类
class SlugMixin(models.Model):
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        abstract = True

