# Generated by Django 4.2.4 on 2023-10-25 03:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("form_handlers", "0007_inquiry_custom_order_inquiry_is_active_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inquiry",
            name="custom_order",
        ),
        migrations.RemoveField(
            model_name="inquiry",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="inquiry",
            name="is_featured",
        ),
    ]
