from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render,redirect
from category.models import Category
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
        print(user)
    else:
        return redirect("vendor_login")
    if request.method == 'POST':
        form = add_product_form(request.POST,request.FILES)
        if form.is_valid:
            product_name = request.POST['product_name']
            category = Category.objects.get(id=request.POST['category'])
            
            discription = request.POST['discription']
            size_chart =Size_chart.objects.get(id=request.POST['size_chart'])
            
            price = request.POST['price']
            image = request.POST['image']
            stock = request.POST['stock']
            slug = slugify(product_name)
            product = Product.objects.create(
                product_name=product_name,
                size_chart=size_chart,
                category=category,
                discription=discription,
                slug = slug,
                price=price,
                image=image,
                stock=stock,
                )
            product.slug=slug
            product.save()
            #verification
            current_site = get_current_site(request)  
            mail_subject = 'Register Your Account'
            message = render_to_string('admin/admin_product_approve.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })  
            to_email = settings.ADMIN_EMAIL
            send_email = mail.EmailMessage(mail_subject,message,settings.EMAIL_HOST_USER,[to_email])  
            send_email.send()
            messages.success(request,'product is requsted to admin.z')
            return redirect('tables')
    else:

        form = add_product_form(initial={'slug': 'no need'})
    

    return render(request,'vendor/pages/add_product.html', {'forms':form,})



def view_product(request,id):
    product_view = Product.objects.get(id = id)
    context = {
        'products_view':product_view,
    }
    return render(request,'vendor/pages/view_product.html',context)


def update_product(request,id):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        category = request.POST['category']
        discription = request.POST['discription']
        size_chart = request.POST['size_chart']
        price = request.POST['price']
        image = request.POST['image']
        slug = slugify(product_name)
        stock = request.POST['stock']
        user = Product.objects.create(
            product_name=product_name,
            size_chart=size_chart,
            category=category,
            discription=discription,
            slug = slug,
            price=price,
            image=image,
            stock=stock,
            )
        user.slug=slug
        user.is_available = True
        user.permition=True
        user.save()

    product_update = Product.objects.get(id=id)
    context={
        'product_update':product_update,
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

