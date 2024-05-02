from django.contrib import admin

from orders.models import Order, OrderItem


# admin.site.register(Order)
# admin.site.register(OrderItem)

class OrderItemTabularAdmin(admin.TabularInline):
    model = OrderItem
    fields = 'product', 'name', 'price', 'quantity'
    search_fields = (
        'product',
        'name',
    )
    extra = 0


class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = (
        'status',
        'is_paid',
        'send_email',
        'created_timestamp',
    )

    search_fields = (
        'status',
        'is_paid',
        'send_email',
        'created_timestamp',
    )
    readonly_fields = ('created_timestamp', 'send_email')
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'product',
        'name',
        'price',
        'quantity',
    )
    search_fields = (
        'order',
        'product',
        'name',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'status',
        'is_paid',
        'send_email',
        'created_timestamp'
    )

    search_fields = (
        'id',
    )

    readonly_fields = ('created_timestamp',)

    list_filter = (
        'id',
        'is_paid',
        'status',
    )
    inlines = (OrderItemTabularAdmin,)
