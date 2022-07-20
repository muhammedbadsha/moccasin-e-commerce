from django.shortcuts import redirect, render
from . forms import AdminLoginForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def admin_home(request):
    return render(request,'admin/admin_home.html')

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_home') 
    if request.method =='POST':
        form = AdminLoginForm(request.POST)
        
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email = email , password = password)
        if user is not None and user.is_admin:
            auth.login(request,user)
            return redirect('admin_home')
        else:
            return redirect('admin_login')
    else:
        form = AdminLoginForm()
        return render(request,'admin/admin_login.html',{'form':form})

@login_required
def admin_logout(request):
    auth.logout(request)
    return redirect('admin_login')




def admin_charts_chartjs(request):
    return render(request,'admin_charts_chartjs.html')


def admin_maps_google(request):
    return render(request,'admin_maps_google.html')

def admin_icons_feather(request):
    return render(request,'admin_icons-feather.html')


def admin_pages_blank(request):
    return render(request,'admin_pages_blank.html')


# def admin_charts_chartjs(request):
#     return render(request,'admin_charts_chartjs.html')


# def admin_charts_chartjs(request):
#     return render(request,'admin_charts_chartjs.html')
