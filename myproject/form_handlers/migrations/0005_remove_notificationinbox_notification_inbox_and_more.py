# Generated by Django 4.2.4 on 2023-10-03 00:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("form_handlers", "0004_notificationinbox_created_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notificationinbox",
            name="notification_inbox",
        ),
        migrations.AddField(
            model_name="notificationinbox",
            name="email",
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]