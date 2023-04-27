from django import forms
from django.forms import ModelForm
from accounts.models import User
from product.models import Product

class VendorForm(ModelForm):
    password = forms.CharField(widget =forms.PasswordInput(attrs={
    'Placeholder': 'Enter password'
    }))
    confirm_password = forms.CharField(widget =forms.PasswordInput(attrs={
    'Placeholder': 'confirm password'
    }))
    first_name=forms.CharField()
    class Meta:
        model = User
        fields = ['first_name','last_name','shop_name','email','phone_number','city','state','zip_code']

    def __init__(self,*args, **kwargs):
        super(VendorForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first_name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last_name'
        self.fields['shop_name'].widget.attrs['placeholder'] = 'Enter shop name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        self.fields['state'].widget.attrs['placeholder'] = 'Enter state'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'enter phone number '
        
        self.fields['city'].widget.attrs['placeholder'] = 'Enter city '
        self.fields['zip_code'].widget.attrs['placeholder']=' enter zip_code'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


    def clean(self):
        cleaned_data = super(VendorForm,self).clean()
        password = cleaned_data.get('password',)
        confirm_password = cleaned_data.get('confirm_password',)
        if password != confirm_password:
            try:
                raise VendorForm(
                    'password does not match!'
                )
            except ValueError as e:
                print(e)

class add_product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'image', 'product_name', 'category', 'stock','size_chart','price', 'discription','product_gen','is_available']
        widgets = {
            "images":forms.ClearableFileInput(attrs={
                "class":"form-control",
                "name":"image",
                "type":"file"
            })
        }

    def __init__ (self,*args,**kwargs):
        super(add_product_form,self).__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if field == 'image':
                self.fields[field].widget.attrs['class']='upload btn btn-primary'
            if field == 'is_available':
                self.fields[field].widget.attrs['class']='checkbox'

        self.fields['product_name'].widget.attrs['placeholder'] = 'product name'
        self.fields['category'].widget.attrs['placeholder'] = ' select..'
        self.fields['stock'].widget.attrs['placeholder'] = ' enter stock less than 20'
        self.fields['price'].widget.attrs['placeholder'] = 'enter within 400 to 10000 rupee'
        self.fields['size_chart'].widget.attrs['placeholder'] = ' select..'
        self.fields['discription'].widget.attrs['placeholder'] = ' enter somthing..'
        
        



            
        
