from django.urls import path
from .import views
urlpatterns = [


    path('shoping_cart',views.shoping_cart,name='shoping_cart'),
    path('priceTotal',views.priceTotal,name='priceTotal'),
    # path('remove_cart_item',views.remove_cart_item,name='remove_cart_item'),
    path('total_of_product_price_qut',views.total_of_product_price_qut,name='total_of_product_price_qut'),
    path('checkout_total',views.checkout_total,name='checkout_total'),
    
    ]
htmx_urlpatterns = [
    path('remove_cart_item/<int:id>/get',views.remove_cart_item,name='remove_cart_item'),
    
]

urlpatterns += htmx_urlpatterns