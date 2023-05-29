# from re import T
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from accounts.models import *
# Create your models here.
# from operator import truth
from django.db import models
from django.urls import reverse
from accounts.models import User
from category.models import Category
from django.core.validators import MinValueValidator,MaxValueValidator
import uuid

product_gender=(
    ("all","all"),
    ("men", "men"),
    ("women", "women"),
    ("kids","kids"),
)




class Size_chart(models.Model):
    size = models.PositiveIntegerField(validators=[MinValueValidator(4),MaxValueValidator(25),],unique=True,null=True)
    class Meta:
        verbose_name = 'size'

    def __str__(self):
        return self.size



class Product(models.Model):
    
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    # uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    product_gen = models.CharField(max_length = 30,choices = product_gender,null=True,default='all')
    product_name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=200,unique=True)
    image = models.ImageField(upload_to='image/', height_field=None, width_field=None, max_length=None, null=True)
    discription = models.TextField(max_length=500,blank=True)
    price = models.PositiveIntegerField(validators=[MinValueValidator(400),MaxValueValidator(10000),],null=True)
    size_chart = models.IntegerField(null = True, blank=True)
    stock = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(20),],null=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='select any one') 
    permition = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
   

   
    

    def __str__(self):
        return self.product_name


    def get_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug])

    
    # @receiver(post_save,sender = user)
    # def create_product_profile(sender,instance,created,**kwrgs):
    #     if created:
    #         User.objects.create(user=instance)


    # @receiver(post_save,sender=user)
    # def save_product_profile(sender,instance,**kwrgs):
    #     instance.profile.save()

    