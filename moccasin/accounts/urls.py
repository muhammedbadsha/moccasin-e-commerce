from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('user_login',views.user_login,name='user_login'),
    path('user_register',views.user_register,name='user_register'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('otp',views.otp,name='otp'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/',views.reset_password_validate,name='reset_password_validate'),
    path('reset_password/',views.reset_password,name='reset_password'),

    
    
    path('blog',views.blog,name='blog'),
    path('order_status',views.order_status,name='order_status'),
    
    path('order_status_click/<id>/',views.order_status_click,name='order_status_click'),
    path('blog_detail',views.blog_detail,name='blog_detail'),

    path('about',views.about,name='about'),
]