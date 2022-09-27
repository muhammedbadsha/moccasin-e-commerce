from importlib.resources import contents
from itertools import count
import json

from django.db.models import Sum
from .models import CartItem
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import CartItem
from django.views.decorators.http import require_http_methods
# Create your views here.


def shoping_cart(request):
    try:

        cartItem=CartItem.objects.filter(customer=request.user).all()
    except:
        cartItem=None

    context={ 
        'cartItem':cartItem,
    }
        
    return render(request,'user/shoping_cart.html',context)

def priceTotal(request):
    data_from_post = json.loads(request.body)
    productQty = data_from_post['qut']
    cartId = data_from_post['cartId']
    print('productQty:',productQty)
    print('cartId:',cartId)
    cart=CartItem.objects.get(id=cartId)
    productPrice=cart.product.price
    print(productPrice)
    totalQtyPrice =  productPrice*int(productQty)
    cart.pro_qty_price=totalQtyPrice
    cart.quantity=productQty
    cart.save()
    
    return JsonResponse('item was added',safe=False)
@require_http_methods(['GET'])
def remove_cart_item(request,id):
    
    try:
        product = get_object_or_404(CartItem ,id= id)
        cart_item = CartItem.objects.filter(id = id)
        cart_item.delete()
        cart = CartItem.objects.all()
        # return redirect('shoping_cart')
    except:
        cart_item=None
        cart=None
    print("iiiiiiiiiiiiiiiiii")
    context={ 
        'cartItem':cart,
    }
    
    return redirect('shoping_cart')


# def remove_cart_item(request):
#     data_from_post = json.loads(request.body)
#     cartId = data_from_post['cartId']
    
#     cart = CartItem.objects.filter(id=cartId)


#     cart.delete()
#     return JsonResponse('item was added',safe=False)


def total_of_product_price_qut(request):
    try:
        all_cart_total = CartItem.objects.filter(customer = request.user).all()
        grand_total = 0
        for i in all_cart_total:
            grand_total += int(i.pro_qty_price)
    except:
        all_cart_total=None
    # print(grand_total)
    data = {
        'grand_total':grand_total,
    }
    
    return JsonResponse(data)


def checkout_total(request):
    data_from_post = json.loads(request.body)
    total_price = data_from_post['total_price']
    print(total_price)
    print('thata')
    data = {
        'total_price':total_price
    }
    return JsonResponse(data)
