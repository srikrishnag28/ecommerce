from django.shortcuts import render, HttpResponse
from store.models import Product, ProductImage


def home(request):

    return render(request, 'home.html')
