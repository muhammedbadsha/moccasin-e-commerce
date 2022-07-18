from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('user_login',views.user_login,name='user_login'),
    path('user_register',views.user_register,name='user_register'),
    path('user_logout',views.user_logout,name='user_logout'),


    path('product',views.product,name='product'),
    
    path('blog',views.blog,name='blog'),
    path('shoping_cart',views.shoping_cart,name='shoping_cart'),
    path('blog_detail',views.blog_detail,name='blog_detail'),

    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
]