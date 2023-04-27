from django import forms 

from .models import Category


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs['class'] = 'form-control'
        self.fields['category_name'].widget.attrs['placeholder'] = 'enter category name'
        
        
    #     self.fields['category_name'].wedget.attrs['class'] = "form-control"