from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from autoslug import AutoSlugField


class Products(models.Model):
    product_name = models.CharField(max_length=101, verbose_name='product_name')
    product_image = models.FileField(null=True, blank=True, upload_to='media/', verbose_name='product_image')
    product_description = models.TextField(verbose_name='product_description')
    product_price = models.IntegerField(verbose_name='product_price')
    slug = AutoSlugField(unique=True, populate_from='product_name')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        if len(self.product_name) > 50:
            self.product_name = self.product_name[:50]  # Trim the name to 50 characters
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.slug)])

