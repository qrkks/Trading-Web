import os
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from abstractapp.models import BaseModel, SlugMixin

# Create your models here.


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
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
        return reverse('category-products', args=[category_path])



class Product(models.Model):
    # 基本信息
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(blank=True, null=True)
    custom_order = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 页面SEO信息
    page_title = models.CharField(max_length=100, null=True, blank=True)
    page_keywords = models.CharField(max_length=100, null=True, blank=True)
    page_description = models.TextField(null=True, blank=True)

    # 产品属性
    model = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    product_code = models.CharField(max_length=100, null=True, blank=True)

    port = models.CharField(max_length=100, null=True, blank=True)
    product_capacity = models.CharField(max_length=100, null=True, blank=True)
    payment_terms = models.CharField(max_length=100, null=True, blank=True)
    transport_package = models.CharField(max_length=100, null=True, blank=True)
    min_order = models.CharField(max_length=100, null=True, blank=True)

    # images = models.ForeignKey(ProductImage,related_name='product',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-is_active','-is_featured', '-custom_order', 'name']



def product_image_path(instance, filename):
    # 构建文件夹路径，使用产品实例的ID作为文件夹名称
    folder_name = str(instance.product.id)
    # 使用 os.path.join 来构建路径
    return os.path.join('products/images', folder_name, filename)



class ProductImage(models.Model):
    image = models.ImageField(upload_to=product_image_path)
    product = models.ForeignKey(
        Product, related_name='images', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.image.url

# 使用信号来处理图片保存：保存图片时自动以ID为名建立新文件夹
@receiver(pre_save, sender=ProductImage)
def product_image_pre_save(sender, instance, **kwargs):
    # 获取关联的产品实例
    product = instance.product
    # 如果产品实例存在并且具有名称字段，则设置图片路径
    if product and product.name:
        folder_name = product.name
        instance.image.field.upload_to = product_image_path

# 在删除产品时同时删除关联的图片
# @receiver(models.signals.post_delete, sender=Product)
# def delete_related_images(sender, instance, **kwargs):
#     related_images = ProductImage.objects.filter(product=instance)
#     for image in related_images:
#         image.delete()