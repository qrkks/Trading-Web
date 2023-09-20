# Generated by Django 4.2.4 on 2023-09-18 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0012_alter_productimage_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["-is_active", "-is_featured", "-custom_order", "name"]
            },
        ),
        migrations.RenameField(
            model_name="productimage",
            old_name="image",
            new_name="images",
        ),
        migrations.AlterField(
            model_name="productimage",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="images",
                to="products.product",
            ),
        ),
    ]