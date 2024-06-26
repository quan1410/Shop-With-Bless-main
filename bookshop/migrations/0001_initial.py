# Generated by Django 5.0.4 on 2024-05-20 00:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("name", models.CharField(db_index=True, max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "ordering": ("name",),
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
                ("name", models.CharField(db_index=True, max_length=200)),
                ("slug", models.SlugField(max_length=200)),
                ("image", models.ImageField(blank=True, upload_to="products/%Y/%m/%d")),
                (
                    "image2",
                    models.ImageField(blank=True, upload_to="products/%Y/%m/%d"),
                ),
                (
                    "image3",
                    models.ImageField(blank=True, upload_to="products/%Y/%m/%d"),
                ),
                ("description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("available", models.BooleanField(default=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="bookshop.category",
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
                "index_together": {("id", "slug")},
            },
        ),
        migrations.CreateModel(
            name="Review",
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
                ("email", models.EmailField(max_length=20)),
                ("rating", models.IntegerField(default=1)),
                ("review_comment", models.TextField(max_length=200)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="bookshop.product",
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
    ]
