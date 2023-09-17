from django.contrib import admin
from .models import Products, Comments


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_image',)
    list_display_links = ('id', 'product_name', 'product_image',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('products', 'user', 'create_date', 'text',)


admin.site.register(Comments, CommentAdmin)
admin.site.register(Products, ProductsAdmin)