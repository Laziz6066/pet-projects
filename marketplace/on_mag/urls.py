from django.urls import path
from .views import *

urlpatterns = [
    path('', CompAccessories.as_view(), name='home'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('add_product', AddProduct.as_view(), name='add_product'),
    ]