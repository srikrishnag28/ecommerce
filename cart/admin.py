from django.contrib import admin
from .models import CartItems, Cart

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_added')


class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')
    list_editable = ('is_active',)


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems, CartItemsAdmin)
