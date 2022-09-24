from django.urls import path
from .import views



urlpatterns = [
    # path('',views.vendor_login,name='vendor_login'),
    path('vendor_home',views.vendor_home,name='vendor_home'),
    path('vendor_logout',views.vendor_logout,name='vendor_logout'),
    path('vendor_register',views.vendor_register,name='vendor_register'),


    path('update_product/<id>/',views.update_product,name='update_product'),
    path('delete_product/<id>/',views.delete_product,name='delete_product'),
    path('search_product/',views.search_product,name='search_product'),
    path('view_product/<id>/',views.view_product,name='view_product'),
    path('billing',views.billing,name='billing'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('product_profile',views.product_profile,name='product_profile'),
    path('rtl',views.rtl,name='rtl'),
    path('tables',views.tables,name='tables'),
    path('virtual_reality',views.virtual_reality,name='virtual_reality'),
    path('rtl',views.rtl,name='rtl'),
    path('add_product',views.add_product,name='add_product'),
    # path('email',views.email,name='email'),
    
    
    ]