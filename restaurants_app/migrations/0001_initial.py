# Generated by Django 4.2.5 on 2023-11-18 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                ("menuId", models.BigAutoField(primary_key=True, serialize=False)),
                ("category", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=255)),
                ("price", models.IntegerField()),
                ("menuPictureUrl", models.TextField(blank=True, null=True)),
                ("popularity", models.BooleanField(default=False)),
                ("createdDate", models.DateTimeField(auto_now_add=True)),
                ("modifiedDate", models.DateTimeField(auto_now=True)),
                ("status", models.CharField(default="일반", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                ("storeId", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("category", models.SmallIntegerField()),
                ("address", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=20)),
                ("content", models.CharField(blank=True, max_length=255, null=True)),
                ("minDeliveryPrice", models.IntegerField()),
                ("deliveryTip", models.IntegerField(default=0)),
                ("minDeliveryTime", models.IntegerField(blank=True, null=True)),
                ("maxDeliveryTime", models.IntegerField(blank=True, null=True)),
                (
                    "rating",
                    models.DecimalField(decimal_places=1, default=0, max_digits=2),
                ),
                ("dibsCount", models.IntegerField(default=0)),
                ("reviewCount", models.IntegerField(default=0)),
                (
                    "operationHours",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("closedDays", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "deliveryAddress",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("createdDate", models.DateTimeField(auto_now_add=True)),
                ("modifiedDate", models.DateTimeField(auto_now=True)),
                ("status", models.CharField(default="일반", max_length=255)),
                (
                    "userId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="restaurant",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MenuOption",
            fields=[
                (
                    "menuOptionId",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("option", models.CharField(max_length=255)),
                ("content", models.CharField(max_length=255)),
                ("price", models.IntegerField()),
                ("createdDate", models.DateTimeField(auto_now_add=True)),
                ("modifiedDate", models.DateTimeField(auto_now=True)),
                ("status", models.CharField(default="일반", max_length=255)),
                (
                    "menuId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurants_app.menu",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="menu",
            name="storeId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="restaurants_app.restaurant",
            ),
        ),
    ]
