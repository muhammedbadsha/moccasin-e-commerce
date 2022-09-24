from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.models import User
from accounts.forms import RegisterForm
from product.models import Product
from django.conf import settings
from . forms import AdminLoginForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.core.mail import send_mail


@login_required
def admin_home(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('user_login')
    if request.user.is_vendor == True:
        return redirect('vendor_home')
    if request.user.user_role=='user':
        return redirect('user_home')
    return render(request,'admin/admin_home.html')

# def admin_login(request):
#     if request.user.is_authenticated:
#         return redirect('admin_home') 
#     if request.method =='POST':
#         form = AdminLoginForm(request.POST)
        
#         email = request.POST['email']
#         password = request.POST['password']
#         user = auth.authenticate(email = email , password = password)
#         if user is not None and user.is_admin:
#             auth.login(request,user)
#             return redirect('admin_home')
#         else:
#             return redirect('admin_login')
#     else:
#         form = AdminLoginForm()
#         return render(request,'admin/admin_login.html',{'form':form})

@login_required
def admin_logout(request):
    auth.logout(request)
    return redirect('user_login')




def admin_approve_req(request):
    return render(request,'admin_approve_req.html')



# testing and pass to the admin approve_or_not page
    
def approve_option(request, uidb64, token):
    try:
        uid  = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request,'please reset your password')
        return redirect('approve_or_not')
    else:
        messages.error(request,'this link has been expired')
        return redirect('user_login')




def approve_or_not(request):
    list = ['agree','dis_agree']
    if request.method == 'POST':
        option = request.POST.getlist('option')
        if option == ['agree']:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            user.is_vendor = True
            user.is_active = True
            user.save()
            messages.success(request,'email send successfully')
            Subject ='MOCASSIN REGISTRATION'
            from_=settings.EMAIL_HOST_USER
            Message = 'your registration success you can login now  '
            retrive = user.email
            send_mail(
                Subject,
                Message,
                from_,[retrive],
                )
            return redirect('user_login')
        elif option == ['dis_agree']:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            messages.error(request,'email send successfully')
            Subject ='MOCASSIN REGISTRATION'
            from_=settings.EMAIL_HOST_USER
            Message = "sorry could't approve you'r registration request "
            retrive=user.email 
            send_mail(
                Subject,
                Message,
                from_,[retrive],
                )
            return redirect('vendor_register')
        else:
            print('invalid entry')


    
    return render(request,'admin/approve_or_not.html')
# product email

def product_approve_option(request, uidb64, token):
    try:
        uid  = urlsafe_base64_decode(uidb64).decode()
        user = Product._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request,'please reset your password')
        return redirect('product_approve_or_not')
    else:
        messages.error(request,'this link has been expired')
        return redirect('tables')


def product_approve_or_not(request):
    list = ['agree','dis_agree']
    if request.method == 'POST':
        option = request.POST.getlist('option')
        if option == ['agree']:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            user.permition = True
            user.save()
            messages.success(request,'product posted  successfully')
            Subject ='MOCASSIN REGISTRATION'
            from_=settings.EMAIL_HOST_USER
            Message = ' posted success'
            retrive = user.email
            send_mail(
                Subject,
                Message,
                from_,[retrive],
                )
            return redirect('tables')


def admin_edit_profile(request,id):
    if request.user.is_authenticated:
        user=request.user
        user_update = User.objects.get(id=id)
    else:
        return redirect("user_login")
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES,instance=user_update)
        if form.is_valid:
            
            form.save()
           

            return redirect('admin_profile')
    else:

        form = RegisterForm(initial={'slug': 'no need'})

    user_details = User.objects.get(id=id)
    form = RegisterForm(instance=user_details)
    
    context={
        'user_update':form,
        'user_details':user_details,
    }

    return render(request,'admin/admin_edit_profile.html',context)

def admin_product_approve(request):
    return render(request,'admin/admin_product_approve.html')

def admin_charts_chartjs(request):
    return render(request,'admin/admin_charts_chartjs.html')


def admin_maps_google(request):
    return render(request,'admin/admin_maps_google.html')

def admin_icons_feather(request):
    return render(request,'admin/admin_icons-feather.html')


def admin_pages_blank(request):
    return render(request,'admin/admin_pages_blank.html')


def admin_pages_blank(request):
    return render(request,'admin/admin_pages_blank.html')


def admin_pages_profile(request):
    return render(request,'admin/admin_pages_profile.html')



def admin_pages_profile(request):
    return render(request,'admin/admin_pages_profile.html')


def admin_profile(request):
    user = User.objects.all()
    context = {
        'user':user,
        }

    return render(request,'admin/admin_profile.html',context)