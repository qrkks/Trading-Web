# Generated by Django 4.2.7 on 2023-12-13 04:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0016_remove_product_product_code_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productimage",
            name="image_size",
        ),
    ]
