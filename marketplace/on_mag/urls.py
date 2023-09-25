from django.urls import path
from .views import *

urlpatterns = [
    path('', CompAccessories.as_view(), name='home'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('add_product', AddProduct.as_view(), name='add_product'),
    path('user/<int:user_id>/update/', UpdateUserView.as_view(), name='update_user'),
    path('add_to_cart/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    ]