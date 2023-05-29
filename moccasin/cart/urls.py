from django.urls import path
from .import views
urlpatterns = [

    path('add_to_cart<int:id>', views.add_to_cart, name = 'add_to_cart'),
    path('shoping_cart',views.shoping_cart,name='shoping_cart'),
    # path('priceTotal',views.priceTotal,name='priceTotal'),
    # path('decrease_updates<int:id>',views.decrease_updates,name = 'decrease_updates'),
    
    # path('increase_updates<int:id>',views.increase_updates,name = 'increase_updates'),
    # path('remove_cart_item',views.remove_cart_item,name='remove_cart_item'),
    path('total_of_product_price_qut',views.total_of_product_price_qut,name='total_of_product_price_qut'),
    path('checkout_total',views.checkout_total,name='checkout_total'),
    
    ]
htmx_urlpatterns = [
    path('remove_cart_item/<int:id>/get',views.remove_cart_item,name='remove_cart_item'),
    path('update_qut_price/',views.update_qut_price,name='update_qut_price'),
]

urlpatterns += htmx_urlpatterns