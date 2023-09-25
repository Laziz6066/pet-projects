from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Products, Cart, CartItem
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout, login
from django.shortcuts import redirect, HttpResponse
from django.views.generic.edit import FormMixin
from django.contrib import messages


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
        comment = form.save(commit=False)
        comment.products = self.get_object()  # Ensure the correct product is associated
        comment.user = self.request.user
        comment.save()

        # Now, add the product to the cart
        product = self.get_object()
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart,
                                                            product=product)  # Use 'product' instead of 'self.object'
        cart_item.quantity += 1
        cart_item.save()

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


class UpdateUserView(UpdateView):
    model = User
    form_class = ProfileUserForm
    template_name = 'on_mag/profile_user.html'

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['user_id'])

    def get_success_url(self):
        return reverse('update_user', kwargs={'user_id': self.object.id})


def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()

    context = {
        'cart_items': cart_items,
        'total_price': cart.total_price(),
    }

    return render(request, 'on_mag/cart.html', context)


def add_to_cart(request, slug):
    product = get_object_or_404(Products, slug=slug)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if cart_item.quantity < product.quantity:
        cart_item.quantity += 1
        cart_item.save()
    else:
        messages.success(request, 'Недостаточно товаров для добавления.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if item.cart.user == request.user:
        item.delete()

    return redirect('view_cart')