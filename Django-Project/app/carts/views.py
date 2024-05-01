from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_list_or_404, redirect
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products
from goods.utils import q_search


def cart_add(request):

    product_id = request.POST.get("product_id")

    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.object.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.object.create(user=request.user, product=product, quantity=1)
    else:
        carts = Cart.object.filter(
            session_key=request.session.session_key, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.object.create(
                session_key=request.session.session_key, product=product, quantity=1)

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', {"carts": user_cart}, request=request)

    response_data = {
        'message': 'Товар добавлен в корзину',
        'cart_items_html': cart_items_html,
    }

    return JsonResponse(response_data)


def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.object.get(id=cart_id)
    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', {"carts": cart}, request=request)

    response_data = {
        'message': 'Колличество изменено',
        'cart_items_html': cart_items_html,
        'quaantity': updated_quantity,
    }

    return JsonResponse(response_data)


def cart_remove(request):

    cart_id = request.POST.get("cart_id")

    cart = Cart.object.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', {"carts": user_cart}, request=request)

    response_data = {
        'message': 'Товар удален',
        'cart_items_html': cart_items_html,
        'quantity_deleted': quantity,
    }

    return JsonResponse(response_data)
