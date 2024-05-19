from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users import views
from users.views import UsersApiView

app_name = 'users'

router = DefaultRouter()
router.register(r"users/", viewset=UsersApiView, basename='user')

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('users-cart/', views.users_cart, name='users_cart'),
    path('logout/', views.logout, name='logout'),
]

urlpatterns += [
    path('', include(router.urls)),
]