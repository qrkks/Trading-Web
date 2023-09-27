from django.db import models
from slugify import slugify

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    custom_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            counter = 1
            while Tag.objects.filter(slug=slug).exists():
                slug = f"{slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
