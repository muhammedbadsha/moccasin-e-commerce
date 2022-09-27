# Generated by Django 4.0.6 on 2022-09-26 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_cashondelivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashondelivery',
            name='product_status',
            field=models.CharField(choices=[('shipping', 'shipping'), ('Picked by courier', 'Picked by courier'), ('On the way', 'On the way'), ('Ready for pickup', 'Ready for pickup'), ('pending', 'pending'), ('delivered', 'delivered'), ('cancel', 'cancel')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_status',
            field=models.CharField(choices=[('shipping', 'shipping'), ('Picked by courier', 'Picked by courier'), ('On the way', 'On the way'), ('Ready for pickup', 'Ready for pickup'), ('pending', 'pending'), ('delivered', 'delivered'), ('cancel', 'cancel')], max_length=50, null=True),
        ),
    ]
