# Generated by Django 4.2.5 on 2023-09-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=101, verbose_name='product_name')),
                ('product_image', models.FileField(blank=True, null=True, upload_to='media/', verbose_name='product_image')),
                ('product_description', models.TextField(verbose_name='product_description')),
                ('product_price', models.IntegerField(verbose_name='product_price')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
