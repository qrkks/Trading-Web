from collections.abc import Iterable
import os
from django.db import models
from django.urls import reverse
from slugify import slugify
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    
    custom_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class MPTTMeta:
        order_insertion_by = ['-custom_order', 'name']

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        url_list = [self.slug]
        parent = self.parent
        while parent:
            url_list.insert(0, parent.slug)
            parent = parent.parent
        # 将列表转换为路径字符串，使用斜杠分隔
        category_path = '/'.join(url_list)
        return reverse('blog-list', args=[category_path])

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


def get_upload_path(instance, filename):
    # 获取文件的扩展名
    ext = filename.split('.')[-1]

    # 这里我们使用slug作为文件名。您可以选择使用其他字段（如title）
    filename = f"{instance.id}.{ext}"

    return os.path.join('blog/images/', filename)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True,blank=True,null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    content = RichTextUploadingField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='blog')

    custom_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self,*args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f'{slug}-{counter}'
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.slug})
    
