# Generated by Django 4.2.7 on 2023-12-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0008_alter_product_created_at_alter_product_is_active_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="productimage",
            name="image_size",
            field=models.FloatField(
                blank=True,
                default=0,
                help_text="Size of the image file in kilobytes (KB)",
                null=True,
            ),
        ),
    ]
