# Generated by Django 4.2.7 on 2023-12-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_alter_product_custom_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="is_featured",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
