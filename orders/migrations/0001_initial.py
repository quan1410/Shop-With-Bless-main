# Generated by Django 5.0.4 on 2024-05-20 00:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bookshop", "0001_initial"),
        ("coupons", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=250)),
                ("phone", models.CharField(max_length=14)),
                ("postal_code", models.CharField(max_length=20)),
                ("city", models.CharField(max_length=100)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("paid", models.BooleanField(default=False)),
                ("braintree_id", models.CharField(blank=True, max_length=150)),
                (
                    "discount",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "coupon",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="orders",
                        to="coupons.coupon",
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="orders.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_items",
                        to="bookshop.product",
                    ),
                ),
            ],
        ),
    ]