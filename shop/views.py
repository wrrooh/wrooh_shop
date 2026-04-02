from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    return HttpResponse("Добро пожаловать в магазин!")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'shop/products.html', {'products': products})

def category_products(request, slug):
    from .models import Category
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/products.html', {'products': products, 'category': category})

def product_detail(request, slug):
    from .models import Product
    product = Product.objects.get(slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})