# Generated by Django 4.0.6 on 2022-09-10 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartitem_pro_qty_price'),
        ('order', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cartItem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cartitem'),
        ),
    ]