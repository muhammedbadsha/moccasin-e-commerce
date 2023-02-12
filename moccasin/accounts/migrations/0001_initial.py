# Generated by Django 4.0.6 on 2023-02-09 11:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_role', models.CharField(choices=[('user', 'user'), ('vendor', 'vendor'), ('admin', 'admin')], max_length=30, null=True)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('shop_name', models.CharField(max_length=100, null=True)),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^\\d\\d\\d\\d\\d\\d\\d\\d\\d\\d$', message='phone number must have 10 digits')], verbose_name='mobile number')),
                ('city', models.CharField(max_length=150, null=True)),
                ('state', models.CharField(max_length=150, null=True)),
                ('zip_code', models.IntegerField(null=True)),
                ('otp', models.CharField(default=True, max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_vendor', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_user', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_address', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
