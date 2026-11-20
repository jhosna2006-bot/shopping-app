from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.filter(is_available=True, stock__gt=0)
    return render(request, "shop/product_list.html", {"products": products})