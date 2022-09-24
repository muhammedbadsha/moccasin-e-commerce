from django import forms
from accounts.models import User
from django.forms import ModelForm


mychoice = (
    ('Agree','Agree'),
    ('Dis Agree','Dis Agree'),
)

class AdminLoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'enter the password'
    }))
    class Meta:
        model = User
        fields = ['email','password']

    def __init__ (self, *args, **kwargs):
        super(AdminLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = "Enter your email"     
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


    def clean(self):
        cleaned_data = super(AdminLoginForm,self).clean()
        email = User.objects.get('email')
        password = User.objects.get('password')
        admin_side = User.objects.filter(is_admin = True)
        if email is not admin_side.email:
            raise forms.ValidationError('you are not the admin ')
        if password is not admin_side.password:
            raise forms.ValidationError('password is incorrect')





class updateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number','user_role']

class updateVendorForm(forms.ModelForm):
    class Meta:
        modal = User
        fields = ['first_name', 'last_name', 'email', 'phone_number','shop_name','user_role','city','state',]