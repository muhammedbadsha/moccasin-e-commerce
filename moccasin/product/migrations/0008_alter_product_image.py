# Generated by Django 4.0.6 on 2023-05-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_image_delete_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
