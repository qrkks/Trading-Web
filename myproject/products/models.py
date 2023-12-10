import random
import string
from django.utils import timezone
import os
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from slugify import slugify
from abstractapp.model_manager import CommonManager
from taggit.managers import TaggableManager

from utils.models import ViewCount
from abstractapp.func import generate_custom_order, generate_slug, resize_and_convert_image

# Create your models here.


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True,null=True,blank=True)
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
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    
class Product(models.Model):

    # 基本信息
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=100,blank=True,null=True,unique=True,db_index=True)
    description = models.TextField(blank=True, null=True,db_index=True)
    custom_order = models.IntegerField(blank=True,null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)
    is_featured = models.BooleanField(default=False,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

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

    # 关联关系
    related_products = models.ManyToManyField('self',blank=True)
    tags = TaggableManager(blank=True)

    # 计数
    view_count = models.OneToOneField(ViewCount,on_delete=models.CASCADE,null=True,blank=True)


    # 分配自定义模型管理器给 objects 属性
    # objects = ProductQueryset().as_manager()
    objects = CommonManager()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-is_active','-is_featured','custom_order','-name']

    def save(self, *args, **kwargs):
        """
        Save the instance to the database.
        
        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        
        # Generate a slug for the instance
        generate_slug(self, *args, **kwargs)
        
        # Generate a custom order for the instance
        generate_custom_order(self, *args, **kwargs)
        
        # Call the save method of the parent class
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        """
        Returns:
            str: The absolute URL of the product detail page.
        """
        # Get the slug of the category and all its ancestors
        category_path = '/'.join([cat.slug for cat in self.category.get_ancestors(include_self=True)])
        
        # Generate the URL using the reverse function and the dynamic category path
        return reverse('product-detail', args=[category_path, self.slug])
        # return reverse('product-detail', kwargs={'category_path': category_path, 'slug': self.slug})




# 定义常量
PRODUCT_IMAGES_PATH = 'products/images'


class ProductImage(models.Model):
    image = models.ImageField(upload_to=PRODUCT_IMAGES_PATH)
    product = models.ForeignKey(
        Product, related_name='images', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.image.url

# 使用信号来处理图片保存：在保存图片前自动以ID为名建立或放入新文件夹
@receiver(pre_save, sender=ProductImage)
def product_image_pre_save(sender, instance, **kwargs):
    """
    Pre-save signal handler for the ProductImage model.
    Sets the image file name and path based on the associated product.

    Args:
        sender: The sender of the signal.
        instance: The instance of the ProductImage being saved.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """

    # Get the associated product from the instance
    product = instance.product

    # Check if the product instance exists and has a name field
    # This ensures that the file name generation logic is only executed when necessary,
    # ensuring code robustness and correctness.
    if product and product.name:

        # Generate a random string of characters
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

        # Split the extension from the image file name
        ext = instance.image.name.split('.')[-1]

        # 获取当前的东八区时间
        now = timezone.now().astimezone(timezone.get_default_timezone())

        # Construct the unique file name based on product information, current timestamp, and random string
        unique_filename = f'{product.name}_{now.strftime("%Y%m%d%H%M")}_{random_string}.{ext}'

        # Set the image name to include the product id and the unique file name
        instance.image.name = os.path.join(str(product.id), unique_filename)

        resize_and_convert_image(instance.image, 1600, 'webp', False, 80)  # 根据需要调整参数
