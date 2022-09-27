from checkout.views import payment
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from cart.models import CartItem
from checkout.models import UserAddress
from product.models import Product
from .models import CashOnDelivery, Payment, order
# Create your views here.
@csrf_exempt
def payment_success(request):
    
    payment_id = request.GET['razorpay_order_id']
    payment_order = Payment.objects.get(payment_id = payment_id)
    payment_order.paid_or_not=True
    payment_order.ordered_or_not = True
    payment_order.status='success'
    payment_order.save()
    cartItem = CartItem.objects.filter(customer=request.user).all()
    user = request.user
    userAddress = UserAddress.objects.get(user=user)
    print(userAddress)
    print(user)
    produ = Product.objects.all()
    if payment_order.paid_or_not==True and payment_order.ordered_or_not == True:
        for products in cartItem:
            order_product = order.objects.create(payment = payment_order,user=user,product = products.product,product_status='shipping',user_address = userAddress)
            order_product.save()
    if payment_order.ordered_or_not==True:
        for i in cartItem:
            # stock_count = 0
            if i.product == produ:
                produ.stock = int(produ.stock)-cartItem.quantity
                print(produ.stock)
                produ.save()

    return render(request,'user/payment_success.html')

def cash_on_delevery(request):
    user = request.user
    user_address= UserAddress.objects.get(user=user)
    produ = Product.objects.all()
    cartItem = CartItem.objects.filter(customer = user).all()
    
    for i in cartItem:

        cash_order_create = CashOnDelivery.objects.create(
            user = user, 
            
            user_address=user_address,
            product = i.product,
            product_status='shipping' 
            )
        cash_order_create.payment_id = True
        cash_order_create.order = True
        cash_order_create.save()
    return render(request,'user/payment_success.html')