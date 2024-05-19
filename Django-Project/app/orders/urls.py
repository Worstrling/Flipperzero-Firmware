from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders import views
from orders.views import OrdersApiView, OrderItemsApiView

app_name = 'orders'

router = DefaultRouter()
router.register(r"orders/", viewset=OrdersApiView, basename='order')
router.register(r"order_items/", viewset=OrderItemsApiView, basename='order_items')

urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
]

urlpatterns += [
    path('', include(router.urls)),
]