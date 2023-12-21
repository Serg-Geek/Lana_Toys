from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    products = Product.objects.order_by('-id')
    return render(request, 'store/index.html', {'title': 'Главная страница Lana_toys', 'products': products})


def about(request):
    return render(request, 'store/about.html')


def catalog(request):
    products = Product.objects.all()  # Получение всех продуктов из вашей модели

    paginator = Paginator(products, 6)  # Разбиение списка продуктов на страницы по 6 элементов
    page = request.GET.get('page')
    try:
        paginated_products = paginator.page(page)
    except PageNotAnInteger:
        paginated_products = paginator.page(1)
    except EmptyPage:
        paginated_products = paginator.page(paginator.num_pages)

    return render(request, 'store/catalog.html', {'products': paginated_products})
# def catalog(request):
#     products = Product.objects.all()
#
#     return render(request, 'store/catalog.html', {'title': 'Каталог', 'products': products})
