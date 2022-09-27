import email
from django.shortcuts import render,redirect
from .models import UserAddress
from cart.models import CartItem
from django.conf import settings 
from order.models import Payment
from django.contrib.auth.decorators import login_required
import razorpay
# Create your views here.

def edit_shipping_address(request,id):
    useraddr = UserAddress.objects.get(id = id)
    if request.method == 'POST':
        user = request.user
        user_name = request.POST['user_name']
        address = request.POST['address']
        Landmark = request.POST['Landmark']
        Phone_number = request.POST['Phone_number']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip']
        user_address = UserAddress.objects.update(
            user = user,
            user_name = user_name,
            address = address,
            landmark = Landmark,
            phone_number = Phone_number,
            city = city,
            state = state,
            zip_code = zip_code,
        )
        
       

        return redirect('payment')
    context = {
        'useraddr':useraddr,
    }
    return render(request,'user/edit_shipping_address.html',context)

def shipping_address(request):
    if request.user.is_address == True:
        return redirect('payment')
    if request.method == 'POST':
        user = request.user
        user_name = request.POST['user_name']
        address = request.POST['address']
        Landmark = request.POST['Landmark']
        Phone_number = request.POST['Phone_number']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip']
        user_address = UserAddress.objects.create(
            user = user,
            user_name = user_name,
            address = address,
            landmark = Landmark,
            phone_number = Phone_number,
            city = city,
            state = state,
            zip_code = zip_code,
        )
        user.is_address = True
        user.save()
        user_address.save()

        return redirect('payment')


    return render(request,'user/shipping_address.html')

@login_required
def payment(request):
    total = 0
    try:
        cartItems = CartItem.objects.filter(customer = request.user).all()
        for product_quantity_price in cartItems:
            
            total += int(product_quantity_price.pro_qty_price)
            
    except:
        cartItems=None
    userAddress = UserAddress.objects.all()
    
    totalpayment = total*100
    if cartItems:
        client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))
        data = { "amount": totalpayment, "currency": "INR", "payment_capture": "1" }
        payment = client.order.create(data=data)
        payment_id = payment['id']
        user = request.user
        
        # payment_method = request.POST.get('paymethod')
        payment_order = Payment.objects.create(payment_id=payment_id,user = user,amount_paid = total)
        payment_order.save()

    context = {
        'totalpayment':totalpayment,
        'keyid':settings.KEY_ID,
        'payment':payment,
        'total':total,
        'cartItems':cartItems,
        'userAddress':userAddress,
    }
    return render(request,'user/payment.html',context)