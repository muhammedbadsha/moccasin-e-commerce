# Generated by Django 4.0.5 on 2022-07-21 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_otp_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
