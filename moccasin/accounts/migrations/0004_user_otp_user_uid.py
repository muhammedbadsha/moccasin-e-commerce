# Generated by Django 4.0.5 on 2022-07-21 23:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_delete_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
