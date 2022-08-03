from django.shortcuts import render, get_object_or_404, redirect

# Index
from myShop.models import Product, Category


def index(request):
    products = Product.objects.all()
    return render(request, 'myshop/index.html', {'products': products})


def details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'myshop/details.html',  {'product': product})
