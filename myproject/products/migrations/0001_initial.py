# Generated by Django 4.2.4 on 2023-10-03 08:39

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import products.models
import taggit.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("utils", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                (
                    "description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("custom_order", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="products.category",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("custom_order", models.IntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                ("is_featured", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("page_title", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "page_keywords",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("page_description", models.TextField(blank=True, null=True)),
                ("model", models.CharField(blank=True, max_length=100, null=True)),
                ("brand", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "product_code",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("port", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "product_capacity",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "payment_terms",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "transport_package",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("min_order", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="products.category",
                    ),
                ),
                (
                    "related_products",
                    models.ManyToManyField(blank=True, to="products.product"),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
                (
                    "view_count",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="utils.viewcount",
                    ),
                ),
            ],
            options={
                "ordering": ["-is_active", "-is_featured", "custom_order", "-name"],
            },
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to=products.models.PRODUCT_IMAGES_PATH),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
