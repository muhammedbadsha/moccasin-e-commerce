from django.contrib import admin
from .models import CashOnDelivery, Payment,order
# Register your models here.
admin.site.register(Payment)
admin.site.register(order)
admin.site.register(CashOnDelivery)