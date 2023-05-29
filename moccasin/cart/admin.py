from django.contrib import admin

from .models import  CartItem

# Register your models here.
class cartAdmin(admin.ModelAdmin):
    list_display = ('product','customer','quantity')
# admin.site.register(Cart)
admin.site.register(CartItem,cartAdmin)
