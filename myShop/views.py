from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from myShop.models import Product, Cart, Order


def index(request):
    products = Product.objects.all()
    return render(request, 'myshop/index.html', {'products': products})


def details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'myshop/details.html', {'product': product})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product)
    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={'slug': slug}))


def cart(request):
    cart, _ = Cart.objects.get_or_create(Cart, user=request.user)

    return render(request, 'myshop/cart.html', context={'orders': cart.orders.all()})


def delete_cart(request):
    if cart := request.user.cart:
        cart.orders.all().delete()
        cart.delete()

    return redirect(reverse("index"))









