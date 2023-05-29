
from tabnanny import verbose
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

    # Create your models here.

class Category(models.Model):
    def validate_catogory_name(self,value):
        if value == Category.objects.filter(category_name = value).exists():
            raise ValidationError(" Category is already added try another one")
        if len(value) < 3 and len(value) > 15:
            raise ValidationError("category should atleast 3 charcter and atmost 15 characters")
        
    category_name = models.CharField(validators=[validate_catogory_name],max_length=50,unique=True)
    discription = models.CharField(max_length=255,blank=True)
    cart_image = models.ImageField(upload_to='photos/categories',blank=True)

    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse("product_by_category",args=[self.slug])


    def __str__(self) :
        return self.category_name