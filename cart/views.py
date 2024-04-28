from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItems
from store.models import Product, ProductImage
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItems.objects.filter(cart=user_cart)
    total_price = 0
    for cart_item in cart_items:
        product = cart_item.product
        quantity = cart_item.quantity
        total_price += quantity * product.price
        cart_item.total_price = quantity * product.price
        product_image = ProductImage.objects.filter(product=product).first()
        if product_image:
            cart_item.image = product_image.image
    tax = (total_price * 18)/100
    grand_total = tax + total_price
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'tax': tax,
        'grand_total': grand_total
    }
    return render(request, 'cart.html', context=context)


@login_required
def add_cart(request, product_id):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=product_id)
    if CartItems.objects.filter(cart=user_cart, product=product).exists():
        cart_item = CartItems.objects.get(cart=user_cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = CartItems.objects.create(cart=user_cart, product=product, quantity=1)
    return redirect('cart')


@login_required
def delete_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItems.objects.get(cart=user_cart, product=product)
    cart_item.delete()
    return redirect('cart')


@login_required
def remove_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItems.objects.get(cart=user_cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


@login_required
def checkout(request):
    user_cart = Cart.objects.get(user=request.user)
    cart_items = CartItems.objects.filter(cart=user_cart)
    total_price = 0
    for cart_item in cart_items:
        product = cart_item.product
        quantity = cart_item.quantity
        total_price += quantity * product.price
        cart_item.total_price = quantity * product.price
        product_image = ProductImage.objects.filter(product=product).first()
        if product_image:
            cart_item.image = product_image.image
    tax = (total_price * 18) / 100
    grand_total = tax + total_price
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'tax': tax,
        'grand_total': grand_total
    }
    return render(request, 'checkout.html', context=context)
