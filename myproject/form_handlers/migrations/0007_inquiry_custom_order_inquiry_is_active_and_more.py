# Generated by Django 4.2.4 on 2023-10-25 03:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("form_handlers", "0006_inquiry_created_at_inquiry_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="inquiry",
            name="custom_order",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="inquiry",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="inquiry",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="notificationinbox",
            name="custom_order",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="notificationinbox",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="notificationinbox",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
    ]
