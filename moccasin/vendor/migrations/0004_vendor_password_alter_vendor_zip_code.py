# Generated by Django 4.0.5 on 2022-07-18 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_rename_pin_code_vendor_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='password',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='zip_code',
            field=models.IntegerField(null=True),
        ),
    ]