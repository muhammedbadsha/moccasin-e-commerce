from django.urls import path
from .import views



urlpatterns = [
    path('vendor_login',views.vendor_login,name='vendor_login'),
    path('vendor_home',views.vendor_home,name='vendor_home'),
    path('vendor_logout',views.vendor_logout,name='vendor_logout'),
    path('vendor_register',views.vendor_register,name='vendor_register'),
    
    ]