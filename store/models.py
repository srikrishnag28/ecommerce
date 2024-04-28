from django.db import models
from category.models import Category
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


def product_image_upload_path(instance, filename):
    # Generate upload path based on product name
    return f'photos/product_images/{instance.product.product_name}/{filename}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_upload_path)

    def __str__(self):
        return f"Image of {self.product.product_name}"
