# Generated by Django 4.0.6 on 2023-05-29 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_cartitem_cart_delete_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='pro_qty_price',
            field=models.IntegerField(),
        ),
    ]