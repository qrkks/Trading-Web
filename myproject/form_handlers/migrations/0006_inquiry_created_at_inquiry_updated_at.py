# Generated by Django 4.2.4 on 2023-10-03 06:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("form_handlers", "0005_remove_notificationinbox_notification_inbox_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="inquiry",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="inquiry",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
