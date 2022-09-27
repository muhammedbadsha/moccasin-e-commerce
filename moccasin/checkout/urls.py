from django.urls import path
from .import views
urlpatterns = [


    path('',views.shipping_address,name='shipping_address'),
    path('payment',views.payment,name='payment'),
    path('edit_shipping_address/<id>',views.edit_shipping_address,name='edit_shipping_address'),
    ]
