from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.order_by('-id')
    return render(request, 'store/index.html', {'title': 'Главная страница Lana_toys', 'products': products})


def about(request):
    return render(request, 'store/about.html')
