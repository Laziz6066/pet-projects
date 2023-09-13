from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Products
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout, login
from django.shortcuts import redirect, HttpResponse
from django.views.generic.edit import FormMixin


class CompAccessories(ListView):
    model = Products
    template_name = "on_mag/products_list.html"
    context_object_name = "accessor"
    paginate_by = 5


class ProductDetail(FormMixin, DetailView):
    model = Products
    template_name = 'on_mag/product-detail.html'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('product-detail', kwargs={'slug': self.get_object().slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.object
        context['comments_products'] = self.object.comments_products.all()
        form_class = CommentForm()

        context['comment_form'] = form_class
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.products = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


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


def logout_user(request):
    logout(request)
    return redirect('home')


class AddProduct(CreateView):
    model = Products
    form_class = AddProductForm
    template_name = 'on_mag/add-product.html'
    success_url = reverse_lazy('home')

