from django.db import models

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=40,null=True,unique=True)
    