from django.db import models
from accounts.models import User
from checkout.models import UserAddress
from product.models import Product
from cart.models import CartItem

# Create your models here.
product_status_choice =  (
    ('shipping','shipping'),
    ('Picked by courier','Picked by courier'),
    ('On the way','On the way'),
    ('Ready for pickup','Ready for pickup'),
    ('pending','pending'),
    ('delivered','delivered'),
    ('cancel','cancel')
    
)

payment_status = (
    ('success','success'),
    ('failed','failed')
)

class Payment(models.Model):
    payment_id = models.CharField(max_length=100)
    cartItem = models.ForeignKey(CartItem,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    paid_or_not = models.BooleanField(default=False)
    ordered_or_not = models.BooleanField(default=False)
    status = models.CharField(max_length = 30,choices = payment_status,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id




class order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    user_address = models.ForeignKey(UserAddress,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_status = models.CharField(choices= product_status_choice,max_length=50,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.product.product_name

    
class CashOnDelivery(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        user_address = models.ForeignKey(UserAddress,on_delete=models.CASCADE)
        product = models.ForeignKey(Product,on_delete=models.CASCADE)
        product_status = models.CharField(choices= product_status_choice,max_length=50,null=True)
        payment = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.product.product_name
    