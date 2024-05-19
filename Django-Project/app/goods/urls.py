"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from goods import views
from goods.views import CategoryApiView, ProductApiView

app_name = 'goods'

router = DefaultRouter()
router.register(r"categories/", viewset=CategoryApiView, basename='category')
router.register(r"products/", viewset=ProductApiView, basename='product')

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<str:product_slug>/', views.product, name='product'),
]

urlpatterns += [
    path('', include(router.urls)),
]
