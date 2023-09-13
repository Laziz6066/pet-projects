import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marketplace.settings")
django.setup()

from on_mag.models import Products

import json


with open('/marketplace/utils/result_list.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data:
    products = Products(
        product_name=item['name'],
        product_image=item['image'],
        product_description=item['description'],
        product_price=item['price']
    )
    products.save()