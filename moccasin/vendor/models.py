from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


my_choices=(
    ("user", "user"),
    ("vendor", "vendor"),
)


class Vendor(models.Model):
    user_role = models.CharField(max_length = 30,choices = my_choices,null=True)
    shop_name = models.CharField(max_length=50,null=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(
        ('mobile number'), max_length=10, unique=True)
    password = models.CharField(max_length=16,null=True)
    city = models.CharField(max_length=150,null=True)
    state = models.CharField(max_length=150,null=True)
    zip_code = models.IntegerField(null=True)
   
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = True)
    is_superadmin = models.BooleanField(default=False)


    class Meta:
        ordering = ['email']



    def _str_(self):
        return self.email

   