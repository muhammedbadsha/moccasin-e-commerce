from random import randint
from django.conf import settings
from django.forms import ValidationError
from cart.models import CartItem
from product.models import Product
from order.models import order
from .forms import RegisterForm
from .models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth
from django.template.loader import render_to_string
from django.core import mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from accounts.mixins import MssageHandler

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
                user.is_user = True
                user.save()
                return redirect('user_login')
            else:
                messages.error(request,"OTP is incorrect!!")
                return redirect('otp')
        except:
           
        # print(user)
            messages.error(request,"phone number doesnot exist!!")
            return redirect('otp')
           
            print(oldotp)
    # messages.error(request,"phone number does't exists!!")

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
        if user is not None and user.is_active and user.is_admin:
            auth.login(request, user)
            # Redirect to a success page.
            return redirect('admin_home')
        if user is not None and user.is_active and user.is_vendor:
            print('this work')
            auth.login(request, user)
            # Redirect to a success page.
            return redirect('vendor_home')
        if user is not None and user.is_active and user.is_user:
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
    home=request.user
    print(home)
    product = Product.objects.all()
    try:
        cart = CartItem.objects.filter(customer = request.user).all()
    except:
        cart=None
    
    context={
        'product':product,
        'cartItem':cart,
    }

    return render(request,'user/home.html',context)


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)

            current_site = get_current_site(request)  
            mail_subject = 'Reset Your Password'
            message = render_to_string('user/email_password.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })  
            to_email = email
            send_email = mail.EmailMessage(mail_subject,message,settings.EMAIL_HOST_USER,[to_email])  
            print(settings.EMAIL_HOST_USER,to_email)
            send_email.send()
           
            
            return redirect('user_login')
        else:
            messages.info(request,'email does not exists')
            return redirect('forgot_password')
    return render(request,'user/forgot_password.html')


def reset_password_validate(request, uidb64, token):
    
    print(uidb64)
    try:
        uid  = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request,'please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request,'this link has been expired')
        return redirect('user_login')
    


def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password= request.POST['confirm_password']
        if password==confirm_password:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,'your password is changed')
            return redirect('user_login')
        else:
            return redirect('forgot_password')
    return render(request,'user/reset_password.html')   






    


# def product(request):
#     return render(request,'user/product.html')

def about(request):
    return render(request,'user/about.html')

def order_status(request):
   
    try:
        user = request.user
        order_product = order.objects.filter(user=user).all()
    except:
        return redirect('home')

    context = {
        "order_product":order_product,
    }
    return render(request,'user/contact.html',context)

     
def order_status_click(request,id):
    print(id)
    return redirect('order_status')

def blog(request):
    return render(request,'user/blog.html')




def blog_detail(request):
    return render(request,'user/blog_detail.html')





# def about(request):
#     return render(request,'user/about.html')


# def about(request):
#     return render(request,'user/about.html')