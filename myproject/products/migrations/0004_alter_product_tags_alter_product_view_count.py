# Generated by Django 4.2.4 on 2023-10-03 11:58

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("utils", "0001_initial"),
        ("products", "0003_product_view_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="view_count",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="utils.viewcount",
            ),
        ),
    ]
