from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import VendorForm
from accounts.models import  User
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
# product add 
from product.forms import ProductForm
from product.models import Product
# verification
from django.template.loader import render_to_string
from django.core import mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
print(settings.ADMIN_EMAIL)



def vendor_login(request):
    if request.user.is_authenticated:
        return redirect('vendor_home')
    if request.method == 'POST':
        email =request.POST['Email']
        password =request.POST['Password']
        print(email,password)
        user = auth.authenticate(email=email,password=password)
        print(user)
        if user is not None and user.is_active and user.is_vendor:
            auth.login(request,user)
            return redirect('vendor_home')
        # return HttpResponse('<h1>Page was found</h1>')
        messages.error(request,'invalid credential')
        return redirect('vendor_login')

    else:
        return render(request,'vendor/vendor_login.html')
    

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
            mail_subject = 'Reset Your Password'
            message = render_to_string('admin/admin_approve_req.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })  
            to_email = settings.ADMIN_EMAIL
            send_email = mail.EmailMessage(mail_subject,message,settings.EMAIL_HOST_USER,[to_email])  
            send_email.send()
            return redirect('vendor_login')

           
    else:
        form = VendorForm()
    
    return render(request,'vendor/vendor_register.html',{'form':form})

@login_required
def vendor_home(request):
    
    return render(request,'vendor/vendor_home.html')

@login_required
def vendor_logout(request):    
    auth.logout(request)
    return redirect('vendor_login')


def billing(request):
    return render(request,'vendor/pages/billing.html')


def dashboard(request):
    return render(request,'vendor/pages/dashboard.html')

def profile(request):
    return render(request,'vendor/pages/profile.html')

def rtl(request):
    return render(request,'vendor/pages/rtl.html')


def tables(request):
    return render(request,'vendor/pages/tables.html')


def virtual_reality(request):
    return render(request,'vendor/pages/virtual_reality.html')



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid:
            product_name = request.POST['product_name']
            category = request.POST['category']
            discription = request.POST['discription']
            product_size = request.POST['product_size']
            price = request.POST['price']
            image = request.POST['image']
            stock = request.POST['stock']
            user = Product.objects.create(
                product_name=product_name,
                category=category,
                discription=discription,
                product_size=product_size,
                price=price,
                image=image,
                stock=stock,
                )
            user.save()
            return redirect('add_product')
    else:

        form = ProductForm()
    

    return render(request,'vendor/pages/add_product.html', {'forms':form,})