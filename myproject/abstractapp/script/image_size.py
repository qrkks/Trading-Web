from products.models import ProductImage  # 确保引入你的模型
from django.core.files.base import ContentFile
from django.db.models import F
import os
from django.conf import settings

# 查询所有image_size为0的ProductImage实例
product_images = ProductImage.objects.filter(image_size=0)

for image in product_images:
    if os.path.isfile(image.image.path):
        print(f"image.path: {image.image.path}")
        try:
            with open(image.image.path, 'rb') as file:
                content = file.read()
                image.image_size = len(content)
                image.save(update_fields=['image_size'])
            print(f"Updated image size for ProductImage ID: {image.id}")
        except IOError as e:
            print(f"Error accessing file for ProductImage ID: {image.id}: {e}")
    else:
        print(f"File not found for ProductImage ID: {image.id} at path: {image.image.path}")



print("Batch process completed.")
