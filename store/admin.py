from django.contrib import admin
from .models import Product, ProductImage
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'category', 'description', 'price', 'stock', 'is_available')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
