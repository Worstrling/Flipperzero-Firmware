from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404, redirect

from carts.models import Cart
from goods.models import Products
from goods.utils import q_search


def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.object.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.object.create(user=request.user, product=product, quantity=1)

    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    ...


def cart_remove(request, product_slug):
    ...
