from django.urls import path
from .import views



urlpatterns = [
    path('',views.vendor_login,name='vendor_login'),
    path('vendor_home',views.vendor_home,name='vendor_home'),
    path('vendor_logout',views.vendor_logout,name='vendor_logout'),
    path('vendor_register',views.vendor_register,name='vendor_register'),


    path('billing',views.billing,name='billing'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('profile',views.profile,name='profile'),
    path('rtl',views.rtl,name='rtl'),
    path('tables',views.tables,name='tables'),
    path('virtual_reality',views.virtual_reality,name='virtual_reality'),
    path('rtl',views.rtl,name='rtl'),
    
    
    ]