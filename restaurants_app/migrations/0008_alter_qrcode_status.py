# Generated by Django 5.0.4 on 2024-06-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants_app', '0007_alter_qrcode_created_date_alter_qrcode_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='status',
            field=models.CharField(default='미반납', max_length=255, verbose_name='상태'),
        ),
    ]
