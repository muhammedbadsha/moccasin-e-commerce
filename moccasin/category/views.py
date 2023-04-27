import json
from django.shortcuts import render, redirect
from .models import Category
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.core.exceptions import ValidationError
from .forms import CategoryForm

# Create your views here.

# @require_http_methods(['POST'])


def add_category(request):
    if request.method == 'POST':
        # forms = CategoryForm(request.POST)
        print('prrrrrrrrrrrr')

        # if forms.is_valid():
        category_name = request.POST.get('category_name')
        print(category_name)
        if Category.objects.filter(category_name=category_name).exists():
            return HttpResponse(status=200, headers={
                'HX-Trigger': json.dumps({
                    "categoryListChanged": None,
                    "showMessage": f"{category_name} already added."
                })
            })
        elif category_name is not None:
            category = Category.objects.create(category_name=category_name)

            return HttpResponse(status=422, headers={
                'HX-trigger': json.dumps({
                    "categoryListChanged": None,
                    'showMessage': f"{category_name} category is successfuly added"
                })
            })
        else:
            # forms = CategoryForm(request.POST)
            return render(request, 'vendor/include/modal_product_addCategory.html')
        
        
