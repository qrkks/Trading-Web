# Generated by Django 4.2.4 on 2023-10-01 07:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0005_homecarouselimage_learn_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homecarouselimage",
            name="learn_more",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]