from datetime import date
from multiprocessing import context
from unicodedata import category
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render,redirect
from category.models import Category
from order.models import CashOnDelivery

from order.models import Payment
from order.models import order
from product.forms import ProductForm
from .forms import VendorForm
from accounts.models import  User
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
# product add 
from .forms import add_product_form
from django.utils.text import slugify
from product.models import Product,Size_chart
# verification
from django.template.loader import render_to_string
from django.core import mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings




# def vendor_login(request):
#     if request.user.is_authenticated:
#         return redirect('vendor_home')
#     if request.method == 'POST':
#         email =request.POST['Email']
#         password =request.POST['Password']
#         print(email,password)
#         user = auth.authenticate(email=email,password=password)
#         print(user)
#         if user is not None and user.is_active and user.is_vendor:
#             auth.login(request,user)
#             return redirect('vendor_home')
#         # return HttpResponse('<h1>Page was found</h1>')
#         messages.error(request,'invalid credential')
#         return redirect('vendor_login')

#     else:
#         return render(request,'vendor/vendor_login.html')
    

def vendor_register(request):
    if request.user.is_authenticated:
        return redirect('vendor_home')
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            shop_name = form.cleaned_data['shop_name']
            email = form.cleaned_data['email']
            username = email.split("@")[0]
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip_code = form.cleaned_data['zip_code']
            user = User.objects.create_user(
                first_name=first_name, 
                last_name=last_name,
                email=email,
                username=username,
                password=password,
                phone_number = phone_number,
            )
            # user.is_active = True
            # user.is_vendor = True
            user.shop_name = shop_name
            user.city = city
            user.state = state
            user.zip_code=zip_code
            user.save()

            #verification
            current_site = get_current_site(request)  
            mail_subject = 'Register Your Account'
            message = render_to_string('admin/admin_approve_req.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })  
            to_email = settings.ADMIN_EMAIL
            send_email = mail.EmailMessage(mail_subject,message,settings.EMAIL_HOST_USER,[to_email])  
            send_email.send()
            return redirect('user_login')

           
    else:
        form = VendorForm()
    
    return render(request,'vendor/vendor_register.html',{'form':form})

@login_required
def vendor_home(request):
    if request.user.is_authenticated:
        if request.user.is_vendor==True:
            pass
        else:
            return redirect('user_login')
    try:
        today = date.today()
        user = request.user
        payment = Payment.objects.filter(user = user).all()
        orderItem = order.objects.all()
        cash_on_delevery = CashOnDelivery.objects.all()
        for i in range(len(orderItem)):
            print(orderItem[i])

        # print(payment)
        total_sales = 0
        today_total_market=0
        for j in range(len(payment)):
            
            if payment[j].paid_or_not == True and payment[j].created_at==today:
                today_total_market = today_total_market + int(payment[j].amount_paid)
                print(payment[j].created_at)

            if payment[j].paid_or_not == True:
                total_sales = total_sales + int(payment[j].amount_paid)



        print(today)
        print(today_total_market)
        
    except:
        pass

    context = {
        'today_total_market':today_total_market,
        'total_sales':total_sales,
    }
    return render(request,'vendor/vendor_home.html',context)

@login_required
def vendor_logout(request):    
    auth.logout(request)
    return redirect('user_login')




def tables(request):
    product = Product.objects.all()
    context = {
        'product':product
    }
    return render(request,'vendor/pages/tables.html',context)

def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('tables')

def search_product(request):
    try:
        product_name=request.POST['product_name']
        product = Product.objects.get(product_name=product_name)
        context = {
            "product":product,
        }
    except:
        return HttpResponse('<h1>this user could not available</h1>')
    return render(request,'vendor/pages/search_tables.html',context)

def add_product(request):
    if request.user.is_authenticated:
        user=request.user
        
    else:
        return redirect("user_login")
    # try:
    if request.method == 'POST':
        form = add_product_form(request.POST,request.FILES)
        if form.is_valid: 
            product_name = request.POST['product_name']
            category = Category.objects.get(category_name=request.POST['category'])
            
            discription = request.POST['discription']
            size_chart =Size_chart.objects.get(size=request.POST['size_chart'])
            print("hiiii")
            price = request.POST['price']
            stock = request.POST['stock']
            image = request.FILES['image']
            product_gen=request.POST['product_gen']
            slug = slugify(product_name)
            if price >= 400 and price <= 10000:
                return ValidationError("this field must be between 400 to 10000")
            if stock >= 1 and stock <= 20:
                return ValidationError("this field must be between 1 to 20")
            
            product = Product.objects.create(
                product_name=product_name,
                category=category,
                discription=discription,
                slug = slug,
                price=price,
                image=image,
                stock=stock,
                product_gen=product_gen,
                size_chart=size_chart,
                )
            product.is_available=True
            product.permition=True
            product.slug=slug
            
            product.save()
            return redirect('tables')
            
    # except :
        
        messages.error(request,'product name is already entered!!' 'try another one')
                
            #verification
            # current_site = get_current_site(request)  
            # mail_subject = 'Register Your Account'
            # message = render_to_string('admin/admin_product_approve.html',{
            #     'user':user,
            #     'domain':current_site,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':default_token_generator.make_token(user),
            # })  
            # to_email = settings.ADMIN_EMAIL
            # send_email = mail.EmailMessage(mail_subject,message,settings.EMAIL_HOST_USER,[to_email])  
            # send_email.send()
            # messages.success(request,'product is requsted to admin.z')

    else:

        form = add_product_form(initial={'slug': 'no need'})
    category = Category.objects.all()
    size_chart = Size_chart.objects.all()
    
    context = {
        'forms':form,
        'category':category,
        'size_chart':size_chart,

    }

    return render(request,'vendor/pages/add_product.html', context)



def view_product(request,id):
    product_view = Product.objects.get(id = id)
    context = {
        'products_view':product_view,
    }
    return render(request,'vendor/pages/view_product.html',context)


def update_product(request,id):
    if request.user.is_authenticated:
        user=request.user
        product_update = Product.objects.get(id=id)
    else:
        return redirect("user_login")
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product_update)
       
        if form.is_valid:
            
            form.save()
           
            
            #verification
            # current_site = get_current_site(request)  
            # mail_subject = 'Register Your Account'
            # message = render_to_string('admin/admin_product_approve.html',{
            #     'user':user,
            #     'domain':current_site,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':default_token_generator.make_token(user),
            # })  
            # to_email = settings.ADMIN_EMAIL
            # send_email = mail.EmailMessage(mail_subject,message,settings.EMAIL_HOST_USER,[to_email])  
            # send_email.send()
            # messages.success(request,'product is requsted to admin.z')
            return redirect('tables')
    else:

        form = add_product_form(initial={'slug': 'no need'})

    product_update = Product.objects.get(id=id)
    form = ProductForm(instance=product_update)
    print(product_update.id)
    context={
        'product_update':form,
        'product_detail':product_update,
    }

    return render(request,'vendor/pages/update_product.html',context)


    


def billing(request):
    return render(request,'vendor/pages/billing.html')


def dashboard(request):
    return render(request,'vendor/pages/dashboard.html')

def product_profile(request):
   
    return render(request,'vendor/pages/profile.html')

def rtl(request):
    return render(request,'vendor/pages/rtl.html')

def virtual_reality(request):
    return render(request,'vendor/pages/virtual_reality.html')

