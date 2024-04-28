from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField()
    cat_image = models.ImageField(upload_to='photos/category')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
