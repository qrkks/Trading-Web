# Generated by Django 4.2.4 on 2023-10-07 01:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_blog_options_blog_is_active_blog_is_featured"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"ordering": ["-custom_order", "-is_featured", "-id"]},
        ),
    ]
