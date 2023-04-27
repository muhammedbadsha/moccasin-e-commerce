from itertools import count
from multiprocessing import context
from cart.models import Cart,CartItem
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse,HttpResponse
import json
from category.models import Category
from .models import Size_chart
from .models import Product
from django.contrib import messages
# Create your views here.


def product(request,category_slug = None):
    category=None
    product=None
    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        products= Product.objects.filter(category=categories,is_available = True)
        product_count=products.count()
        if products.stock < 1:
            messages.INFO(request,'OUT OF STOCK')
    else:
        product = Product.objects.all().filter(
            is_available = True,
            permition = True,
            )
    try:
        cart = CartItem.objects.filter(customer = request.user).all()
        
    except:
        cart=None
    # if cart is None:
    #     pass
    # else:
    #     # total = 0
    #     # for i in cart:
    #     #     total += i.pro_qty_price
    #     #     print(total)
    context={
        'product':product,
        
        
    }
    
    return render(request,'user/product.html',context)
 

def updateItem(request):
    data_from_post = json.loads(request.body)
    productId = data_from_post['productId']
    action = data_from_post['action']
    quantity = data_from_post['quantity']
    # price = data_from_post['price']

    
    product = Product.objects.get(id = productId)
    # 
    productPrice = product.price
    pro_qty_price=int(productPrice)*int(quantity)
    pro_qty_price=pro_qty_price
    customername= request.user
    print(customername)
    # cart,created= Cart.objects.get_or_create(customer=customername,complete=False) 
    cartItem,created=CartItem.objects.get_or_create(customer=customername,product=product,quantity=quantity,pro_qty_price=pro_qty_price)
    
    # cartItem.save()

    
    return JsonResponse('item was added',safe=False)

def product_size(request):
    if request.method == 'POST':
       
        print('prrrrrrrrrrrr')

        size_prow = request.POST.get('product_size')
        if size_prow is not None :

            size_pro = int(size_prow)
            print(size_pro)
            if size_pro >= 4 and size_pro <= 25:
                if Size_chart.objects.filter(size=size_pro).exists():

                    return HttpResponse(status=200, headers={
                        'HX-Trigger': json.dumps({
                            "categoryListChanged": None,
                            "showMessage": f"{size_pro} already added."
                        })
                    })
                
                else:
                    print('its creates')
                    category = Size_chart.objects.create(size=size_pro)
                    return HttpResponse(status=200, headers={
                        'HX-trigger': json.dumps({
                            "SizeListChanged": None,
                            'showMessage': f"{size_pro} size is successfuly added"
                        })
                    })
            else:
                print('without size')
                return HttpResponse(status=200, headers={
                        'HX-trigger': json.dumps({
                            "SizeListChanged": None,
                            'showMessage': f"{size_pro} is not valid size please enter within 4 to 25"
                        })
                    })
        else:
            # forms = CategoryForm(request.POST)
            return render(request, 'vendor/include/modal_product_addSize.html')