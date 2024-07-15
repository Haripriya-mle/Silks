# products/views.py

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.filter(status=1, is_active=True)
    return render(request, 'products/product_list.html', {'products': products})