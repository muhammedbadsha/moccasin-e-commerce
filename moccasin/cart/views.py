from importlib.resources import contents
from itertools import count
import json
from django.db import models
from django.db.models import Sum
from .models import CartItem
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import JsonResponse
from .models import CartItem
from django.views.decorators.http import require_http_methods
from product.models import Product
# Create your views here.

def add_to_cart(request,id):
    if request.user.is_authenticated:
        if CartItem.objects.filter(product = id,customer = request.user).exists():
            if request.method == "POST":
                print('this dublicut workd')
                quantity = int(request.POST.get('quantity'))

                cartItem = get_object_or_404(CartItem,product = id)
                cartItem.quantity += quantity
                cartItem.save()
               
                return HttpResponse(status=200, headers={
                'HX-Trigger': json.dumps({
                    "categoryListChanged": None,
                    "showMessage": f"{cartItem.product.product_name} product is already added updated the quantity."
                })  
            })
        if request.method == 'POST':
            product = get_object_or_404(Product,id = id)
            print("add new worked")
            user = request.user
            price = product.price
            quantity = request.POST.get("quantity")
            # cart = Cart.objects.create()
            cartItem = CartItem.objects.create(product=product, customer= user, pro_qty_price=price, quantity=quantity)
            
           
        
        return HttpResponse(status=200, headers={
                'HX-Trigger': json.dumps({
                    "categoryListChanged": None,
                    "showMessage": f'{product.product_name}  cart is addded successfully',
                })  
            })
    

    return redirect('user_login')

def shoping_cart(request):
    try:
        user = request.user
        # cartItem = get_object_or_404(CartItem,customer = user)
        cartItem=CartItem.objects.filter(customer = user).all()
        sum = CartItem.get_total_bill(request.user)
    except:
        cartItem=None

   

    context={ 
        'cartItem':cartItem,
        'sub_total_bill':sum,
    }
        
    return render(request,'user/shoping_cart.html',context)

# def priceTotal(request):
#     data_from_post = json.loads(request.body)
#     productQty = data_from_post['qut']
#     cartId = data_from_post['cartId']
#     print('productQty:',productQty)
#     print('cartId:',cartId)
#     cart=CartItem.objects.get(id=cartId)
#     productPrice=cart.product.price
#     print(productPrice)
#     totalQtyPrice =  productPrice*int(productQty)
#     cart.pro_qty_price=totalQtyPrice
#     cart.quantity=productQty
#     cart.save()
    
#     return JsonResponse('item was added',safe=False)

def update_qut_price(request):
    print('update_qut_price')
    data_from_post = json.loads(request.body)
    # productQty = int(data_from_post['qut'])
    cartId = data_from_post['cartId']
    count = int(data_from_post['count'])
    cart = get_object_or_404(CartItem,id = cartId)
    product = get_object_or_404(Product,product_name = cart.product.product_name)
    price = cart.product.price
    
    
    sum = CartItem.get_total_bill(request.user)
    product_qt_mul_value = cart.quantity * price
    if count == -1:
        if cart.quantity == 1 and count == -1:
            print(cart.quantity,count,"firstworked")
            json_response = {
                'productQty':cart.quantity,
                'product_qt_mul_value':product_qt_mul_value,
                'cartId':cartId,
                'sum':sum,
            }
            return JsonResponse(json_response)
        elif product.stock != 1 and count == -1:

            product.stock += 1
            product.save()
            cart.quantity += count
            product_qt_mul_value = cart.quantity * price
            cart.pro_qty_price = product_qt_mul_value
            cart.save()
            print(cart.quantity,count,'secondworked')
            sum = CartItem.get_total_bill(request.user)
            json_response = {
                'productQty':cart.quantity,
                'product_qt_mul_value':product_qt_mul_value,
                'cartId':cartId,
                'sum':sum,
            }
            return JsonResponse(json_response)
        
        elif product.stock == 1 and count == -1:
            product.stock += 1
            product.save()
            cart.quantity += count
            product_qt_mul_value = cart.quantity * price
            cart.pro_qty_price = product_qt_mul_value
            cart.save()
            print(cart.quantity,count,'thered workd')
            sum = CartItem.get_total_bill(request.user)
            json_response = {
                'productQty':cart.quantity,
                'product_qt_mul_value':product_qt_mul_value,
                'cartId':cartId,
                'sum':sum,
            }
            return JsonResponse(json_response)
    else:
        if product.stock != 1 and count == 1:
            product.stock -= 1
            product.save()
            cart.quantity += count

            product_qt_mul_value = cart.quantity * price
            cart.pro_qty_price = product_qt_mul_value
            cart.save()
            print(cart.quantity,count,'fourth workd')
            
            print((cart.pro_qty_price))
            sum = CartItem.get_total_bill(request.user)
            json_response = {
                'productQty':cart.quantity,
                'product_qt_mul_value':product_qt_mul_value,
                'cartId':cartId,
                'sum':sum,
            }
            return JsonResponse(json_response)
        elif product.stock == 1 and count == 1:
            product_qt_mul_value = cart.quantity * price
            cart.pro_qty_price = product_qt_mul_value
            cart.save()
            print(cart.quantity,count,'fifth workd')
            print((cart.pro_qty_price))
            sum = CartItem.get_total_bill(request.user)
            json_response = {
                'productQty':cart.quantity,
                'product_qt_mul_value':product_qt_mul_value,
                'cartId':cartId,
                'sum':sum,
            }
            return JsonResponse(json_response)
        # productQty += count
        # product_qt_mul_value = productQty * price
        # print((cart.pro_qty_price))
        # sum = CartItem.get_total_bill(request.user)
        
    # sum = CartItem.objects.aggregate(total_bill = Sum('pro_qty_price', output_field=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)))['total_bill']
    # print(sum)
    # print(count,productQty,cartId)
    return JsonResponse('this item was worked',safe=False)


# def increase_updates(request,id):
#     cart = CartItem.objects.get(id = id)
#     product = Product.objects.get(product_name = cart.product)
#     print(product)
    
#     if product.stock == 1:
#         print("stock is limitteed")
#         json_data = {'stock':False,
#                      'counting':1,
#                      "rqu" : 0,
#                      'id':id,
#                      'cart_total' :cart.pro_qty_price}
#         return JsonResponse(json_data,safe=False)
#     else:
#         product.stock -= 1
#         product.save()
#         cart.quantity += 1
#         cart.pro_qty_price = cart.product.price * cart.quantity
#         cart.save()
#         json_data = {'stock':True,
#                     'counting':1,
#                     "rqu" : 0,
#                     'id':id,
#                     'cart_total' :cart.pro_qty_price}
#         return JsonResponse( json_data,safe=False)

# def decrease_updates(request,id):
#     cart = CartItem.objects.get(id = id)
#     if cart.quantity == 1:
#         # cart.delete()
#         product_price = cart.product.price
#         json_data = {'stock':True,
#                       'counting':-1,
#                       "rqu" : 0,
#                       'id':id,
#                      'message':'out of stock',
#                      'cart_total' :product_price}
#         return JsonResponse( json_data,safe=False)
#     else:
#         cart.quantity -= 1
#         cart.product.stock += 1
#         cart.pro_qty_price = cart.product.price * cart.quantity
#         cart.save()
#         json_data = {'stock':True,
#                       'counting':-1,
#                       "rqu" : 0,
#                       'id':id,
#                      'cart_total' :cart.pro_qty_price}
#         return JsonResponse( json_data,safe=False)
    # return JsonResponse( cart.pro_qty_price,safe=False)
    
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
    # print("iiiiiiiiiiiiiiiiii")
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
    # print(total_price)
    print('thata')
    data = {
        'total_price':total_price
    }
    return JsonResponse(data)
