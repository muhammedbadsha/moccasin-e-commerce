from django.urls import path
from .import views

urlpatterns = [
    path('admin_home',views.admin_home,name='admin_home'),
    path('',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),


    path('admin_charts_chartjs',views.admin_charts_chartjs,name='admin_charts_chartjs'),
    path('admin_icons_feather',views.admin_icons_feather,name='admin_icons_feather'),
    path('admin_maps_google',views.admin_maps_google,name='admin_maps_google'),

    path('admin_pages_blank',views.admin_pages_blank,name='admin_pages_blank'),
    path('admin_pages_profile',views.admin_pages_profile,name='admin_pages_profile'),
    path('admin_profile',views.admin_profile,name='admin_profile'),
]