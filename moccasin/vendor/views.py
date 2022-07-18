from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import VendorForm
from accounts.models import  User
from django.contrib import auth,messages
# Create your views here.



def vendor_home(request):
    return render(request,'vendor/vendor_home.html')


def vendor_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        vendor = auth.authenticate(email=email, password=password)
        print(vendor)
        if vendor.is_vendor:
            auth.login(request, vendor)
            # Redirect to a success page.
            return redirect('vendor_home')
            
        else:
            # Return an 'invalid login' error message.
          
            messages.error(request,'email and password invalid')
            return redirect('vendor_login')

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
            vendor = User.objects.create_vendor(
                shop_name=shop_name,
                email=email,
                username=username,
                phone_number=phone_number,
                password = password,
                city=city,
                state=state,
                zip_code=zip_code,
            )

           
    else:
        form = VendorForm()
    
    return render(request,'vendor/vendor_register.html',{'form':form})



def vendor_logout(request):
    return redirect('vendor/login')