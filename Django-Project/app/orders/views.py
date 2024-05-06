from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import render, redirect

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.object.filter(user=user)

                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            send_email=form.cleaned_data['email']
                        )
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f"Недостаточное кол-во товара {name} "
                                                      f"В наличии - {product.quantity}")

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('cart:order')

    else:
        initial = {
            'email': request.user.email,
        }
        form = CreateOrderForm(initial=initial)
    context = {
        'title': 'Главная - Оформление заказа',
        'form': form,
        'order': True,
    }
    return render(request, 'orders/create_order.html', context=context)