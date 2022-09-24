from django.urls import path
from .import views

urlpatterns = [
    path('',views.admin_home,name='admin_home'),
    # path('',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),

    # user table controls
    path('admin_edit_profile/<id>',views.admin_edit_profile,name='admin_edit_profile'),


    path('admin_charts_chartjs',views.admin_charts_chartjs,name='admin_charts_chartjs'),
    path('admin_icons_feather',views.admin_icons_feather,name='admin_icons_feather'),
    path('admin_maps_google',views.admin_maps_google,name='admin_maps_google'),

    path('admin_pages_blank',views.admin_pages_blank,name='admin_pages_blank'),
    path('admin_pages_profile',views.admin_pages_profile,name='admin_pages_profile'),
    path('admin_profile',views.admin_profile,name='admin_profile'),

    #email request section
    path('admin_approve_req',views.admin_approve_req,name='admin_approve_req'),
    path('approve_option/<uidb64>/<token>/',views.approve_option,name='approve_option'),
    path('approve_or_not',views.approve_or_not,name='approve_or_not'),

    #product activation
    path('admin_product_approve',views.admin_product_approve,name='admin_product_approve'),
    path('product_approve_option/<uidb64>/<token>/',views.product_approve_option,name='product_approve_option'),
    path('product_approve_or_not',views.product_approve_or_not,name='product_approve_or_not'), 

]