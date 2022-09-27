from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    image=forms.ImageField()
    class Meta:
        model = Product
        fields = ['product_name','category','discription','size_chart','product_gen','price','image','stock']


        