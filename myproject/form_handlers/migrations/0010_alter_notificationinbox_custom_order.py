# Generated by Django 4.2.7 on 2023-11-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("form_handlers", "0009_alter_notificationinbox_custom_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notificationinbox",
            name="custom_order",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]