from django.contrib import admin

from .models import Product, Size_chart
# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','size_chart','category','is_available')
    prepopulated_fields = {'slug':('product_name',)}
admin.site.register(Product,productAdmin)
admin.site.register(Size_chart)