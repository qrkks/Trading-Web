# Generated by Django 4.2.7 on 2023-12-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0014_alter_category_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="code",
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="code",
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
