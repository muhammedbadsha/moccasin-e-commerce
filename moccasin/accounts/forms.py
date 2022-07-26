
from .models import User
from django import forms
from django.forms import Form, ModelForm, PasswordInput, ValidationError



# creating modelform of the same as in models
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget =forms.PasswordInput(attrs={
    'Placeholder': 'Enter password'
    }))
    confirm_password = forms.CharField(widget =forms.PasswordInput(attrs={
    'Placeholder': 'confirm password'
    }))
    
    class Meta:
        model = User
        fields =  ['first_name', 'last_name', 'email', 'phone_number']

    def __init__(self,*args, **kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first_name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last_name'
        # self.fields['username'].widget.attrs['placeholder'] = 'Enter username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email '
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone number'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    # checking password and confirm password is match or not

    def clean(self):
            cleaned_data = super(RegisterForm,self).clean()
            password = cleaned_data.get('password',)
            confirm_password = cleaned_data.get('confirm_password',)
            if password != confirm_password:
                raise ValidationError(
                    'password does not match!'
                )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number']
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



    

