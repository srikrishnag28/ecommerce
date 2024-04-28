from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage
from category.models import Category
from django.core.paginator import Paginator
from collections import defaultdict
# Create your views here.


def store(request, category_slug=None):
    product_images = ProductImage.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product_images = product_images.filter(product__category=category)
    keyword = request.GET.get('keyword')
    if keyword:
        keyword = request.GET['keyword']
        product_with_keyword = Product.objects.filter(description__icontains=keyword)
        product_images = ProductImage.objects.filter(product__in=product_with_keyword)
    products = {}
    for product_image in product_images:
        product = product_image.product
        if product not in products:
            products[product] = []
        products[product].append(product_image)

    products_list = list(products.items())

    paginator = Paginator(products_list, 4)
    page_number = request.GET.get("page")
    products_paginated = paginator.get_page(page_number)

    context = {
        'products': products_paginated,
        'items_count': len(products_list)
    }
    return render(request, 'store.html', context=context)


def product_details(request, category_slug=None, product_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, category=category, slug=product_slug)
    product_images = ProductImage.objects.filter(product=product)
    context = {
        'product': product,
        'product_images': product_images,
    }
    return render(request, 'product_details.html', context=context)



