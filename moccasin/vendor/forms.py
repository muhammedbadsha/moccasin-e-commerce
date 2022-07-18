from django import forms
from django.forms import ModelForm
from .models import Vendor

class VendorForm(ModelForm):
    password = forms.CharField(widget =forms.PasswordInput(attrs={
    'Placeholder': 'Enter password'
    }))
    confirm_password = forms.CharField(widget =forms.PasswordInput(attrs={
    'Placeholder': 'confirm password'
    }))
    class Meta:
        model = Vendor
        fields = ['shop_name','email','phone_number','city','state','zip_code']

    def __init__(self,*args, **kwargs):
        super(VendorForm,self).__init__(*args,**kwargs)
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
            raise VendorForm(
                'password does not match!'
            )


