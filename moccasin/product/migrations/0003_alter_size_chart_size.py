# Generated by Django 4.0.6 on 2023-04-27 01:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_images_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size_chart',
            name='size',
            field=models.PositiveIntegerField(null=True, unique=True, validators=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(25)]),
        ),
    ]
