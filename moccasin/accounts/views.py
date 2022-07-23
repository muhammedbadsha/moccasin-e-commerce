from random import randint
from .mixins import MssageHandler
from .forms import RegisterForm
from .models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth


# Create your views here.
def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            print(email)
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            phone_number = form.cleaned_data['phone_number']
            user = User.objects.create_user(
                first_name=first_name, 
                last_name=last_name,
                email=email,
                username=username,
                password=password,
                phone_number = phone_number,
            )
            user.otp = str(randint(1000,9999))
            user.save()
            print(user.otp,user.phone_number)
            message_handler = MssageHandler(user.phone_number,user.otp).send_otp_to_phone()
            return redirect('otp')
            

         
            return redirect('user_login')
        

    else:
        form = RegisterForm()
    return render(request,'user/user_register.html',{'form':form})


def otp(request):

    if request.method == 'POST':
        
        phone_number = request.POST['phone_number']
        try:
            user = User.objects.get(phone_number = phone_number)
            oldotp=user.otp
            otp = request.POST['otp']
            if otp == oldotp:
                user.is_active = True
                user.save()
                return redirect('user_login')
            else:
                return redirect('otp')
        except:
        # print(user)
            messages.error(request,"user does't exists!!")
            return redirect('otp')
           
        # print(oldotp)
           

    return render(request,'user/user_otp.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
     
    if request.method == 'POST':
        email = request.POST.get('email',None)
        password = request.POST['password']
        print(email,password)
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None and user.is_active:
            auth.login(request, user)
            # Redirect to a success page.
            return redirect('home')
            
        else:
            # Return an 'invalid login' error message.
          
            messages.error(request,'email and password invalid')
            return redirect('user_login')
            
           

    return render(request,'user/user_login.html')


def user_logout(request):
    
    auth.logout(request)
    return redirect('user_login')


# @login_required
def home(request):

    return render(request,'user/home.html')





    


def product(request):
    return render(request,'user/product.html')

def about(request):
    return render(request,'user/about.html')

def contact(request):
    return render(request,'user/contact.html')

def blog(request):
    return render(request,'user/blog.html')


def shoping_cart(request):
    return render(request,'user/shoping_cart.html')


def blog_detail(request):
    return render(request,'user/blog_detail.html')


# def about(request):
#     return render(request,'user/about.html')


# def about(request):
#     return render(request,'user/about.html')


# def about(request):
#     return render(request,'user/about.html')