from django.contrib import admin
from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name',)
    list_display_links = ('id', 'product_name',)


admin.site.register(Products, ProductsAdmin)