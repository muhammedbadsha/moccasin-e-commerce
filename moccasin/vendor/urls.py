from django.urls import path
from .import views



urlpatterns = [
    path('vendor_login',views.vendor_login,name='vendor_login'),
    path('vendor_home',views.vendor_home,name='vendor_home'),
    path('vendor_logout',views.vendor_logout,name='vendor_logout'),
    path('vendor_register',views.vendor_register,name='vendor_register'),


    path('vendor_collection',views.vendor_collection,name='vendor_collection'),
    path('vendor_racing_boots',views.vendor_racing_boots,name='vendor_racing_boots'),
    path('vendor_shoes',views.vendor_shoes,name='vendor_shoes'),
    path('vendor_contact',views.vendor_contact,name='vendor_contact'),
    
    
    
    ]