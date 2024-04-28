from cart.models import Cart, CartItems
from store.models import Product


def cart_count(request):
    cnt = 0
    if request.user.is_authenticated:
        user_cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        user_cart = None
    if user_cart:
        cart_items = CartItems.objects.filter(cart=user_cart)
        for cart_item in cart_items:
            cnt += cart_item.quantity
    return dict(cnt=cnt)
