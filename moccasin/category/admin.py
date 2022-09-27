from django.contrib import admin
from .models import Category
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    prepopulated_fields = {'slug':('category_name',)}

admin.site.register(Category,categoryAdmin)