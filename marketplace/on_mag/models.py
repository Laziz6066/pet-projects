from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class Products(models.Model):
    product_name = models.CharField(max_length=101, verbose_name='product_name')
    product_image = models.FileField(null=True, blank=True, upload_to='static/', verbose_name='product_image')
    product_description = models.TextField(verbose_name='product_description')
    product_price = models.IntegerField(verbose_name='product_price')
    slug = AutoSlugField(unique=True, populate_from='product_name')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        if len(self.product_name) > 50:
            self.product_name = self.product_name[:50]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.slug)])

    def __str__(self):
        return self.product_name


class Comments(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='product',
                                 related_name='comments_products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='comments_text')
