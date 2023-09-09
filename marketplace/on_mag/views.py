from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Products
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout, login
from django.shortcuts import redirect


class CompAccessories(ListView):
    model = Products
    template_name = "on_mag/products_list.html"
    context_object_name = "accessor"


class ProductDetail(DetailView):
    model = Products
    template_name = 'on_mag/product-detail.html'
    context_object_name = 'product'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'on_mag/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'on_mag/login.html'

    # def get_success_url(self):
    #     return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')