# Generated by Django 4.2.4 on 2023-09-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0015_alter_product_slug_alter_productimage_product"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["custom_order", "-name"]},
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]