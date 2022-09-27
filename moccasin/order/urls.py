from django.urls import path
from .import views
urlpatterns = [
    path('',views.payment_success,name='payment_success'),
    path('cash_on_delevery',views.cash_on_delevery,name='cash_on_delevery'),
    
]
