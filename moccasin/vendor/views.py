from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import VendorForm
from .models import  Vendor
from django.contrib import auth
# Create your views here.



def vendor_home(request):
    return render(request,'vendor/vendor_home.html')


def vendor_login(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        vendor = auth.authenticate(email = email, password = password)
        try:
            if vendor is not None:
                auth.login(request,vendor)
        except:
                return redirect('vendor_home')

    else:
        return render(request,'vendor/vendor_login.html')

def vendor_register(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            shop_name = form.cleaned_data['shop_name']
            email = form.cleaned_data['email']
            username = email.split("@")[0]
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip_code = form.cleaned_data['zip_code']
            vendor = Vendor.objects.create(
                shop_name=shop_name,
                email=email,
                username=username,
                phone_number=phone_number,
                password = password,
                city=city,
                state=state,
                zip_code=zip_code,
            )

            vendor.save()
    else:
        form = VendorForm()
    
    return render(request,'vendor/vendor_register.html',{'form':form})



def vendor_logout(request):
    return redirect('vendor/login')