# Generated by Django 4.0.5 on 2022-07-19 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_vendor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]