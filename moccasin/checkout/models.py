from django.db import models
from accounts.models import User
# Create your models here.


class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    user_name=models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    landmark = models.CharField(max_length=50,blank=True)
    phone_number=models.CharField(max_length=50 , null=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    zip_code = models.IntegerField()

    def __str__(self):
        return self.user_name