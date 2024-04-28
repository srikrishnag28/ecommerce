from django.db import models
from store.models import Product
from accounts.models import Account
# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"Cart of {self.user.username}"
        else:
            return "Guest Cart"


class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.product_name

