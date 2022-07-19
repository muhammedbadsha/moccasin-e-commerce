from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import VendorForm
from accounts.models import  User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.




def vendor_login(request):
    # if request.vendor.is_authenticated:
    #     return redirect('vendor_home')
    if request.method == 'POST':
        email =request.POST['Email']
        password =request.POST['Password']
        print(email,password)
        user = auth.authenticate(email=email,password=password)
        if user is not None and user.is_vendor:
            auth.login(request,user)
            return redirect('vendor_home')

    else:
        return render(request,'vendor/vendor_login.html')
    

def vendor_register(request):
    # if request.vendor.is_authenticated:
    #     return redirect('vendor_home')
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
            user.is_vendor = True
            user.shop_name = shop_name
            user.city = city
            user.state = state
            user.zip_code=zip_code
            user.save()
            return redirect('vendor_login')

           
    else:
        form = VendorForm()
    
    return render(request,'vendor/vendor_register.html',{'form':form})

# @login_required
def vendor_home(request):
    
    return render(request,'vendor/vendor_home.html')


    

# @login_required
def vendor_logout(request):    
    auth.logout(request)
    return render(request,'vendor/vendor_login.html')


def vendor_contact(request):
    return render(request,'vendor/contact.html')


def vendor_collection(request):
    return render(request,'vendor/collection.html')

def vendor_racing_boots(request):
    return render(request,'vendor/racing_boots.html')

def vendor_shoes(request):
    return render(request,'vendor/shoes.html')