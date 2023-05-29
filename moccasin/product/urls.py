from django.urls import path
from .views import updateItem,product,product_size


urlpatterns = [
    path('',product,name='product'),
    # path('<slug:category_slug>/',product,name='product_by_category'),
    path('updateItem',updateItem,name='updateItem'),
    path('product_size',product_size,name='product_size'),
    ]