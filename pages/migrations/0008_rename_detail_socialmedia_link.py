# Generated by Django 4.2.4 on 2023-10-03 04:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0007_contactinformation_socialmedia"),
    ]

    operations = [
        migrations.RenameField(
            model_name="socialmedia",
            old_name="detail",
            new_name="link",
        ),
    ]
