from django.db import models
from accounts.models import User
from product.models import Product
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=100,blank=True,unique=True)
    # customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null = True)
    quantity = models.IntegerField()
    pro_qty_price=models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)


    def sub_total(self):
        return self.product.price* self.quantity



    def __unicode__(self):
        return self.product

