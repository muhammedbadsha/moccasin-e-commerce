from django.shortcuts import redirect, render

# Create your views here.
def admin_home(request):
    return render(request,'admin/admin_home.html')

def admin_login(request):
    return render(request,'admin/admin_login.html')

def admin_logout(request):
    return redirect('admin_login')