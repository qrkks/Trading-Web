# Generated by Django 4.2.7 on 2023-12-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0018_productimage_image_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimage",
            name="image_size",
            field=models.PositiveIntegerField(
                blank=True,
                default=0,
                help_text="Size of the image file in bytes",
                null=True,
            ),
        ),
    ]
