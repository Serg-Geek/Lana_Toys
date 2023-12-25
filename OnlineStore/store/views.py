from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import requests


def index(request):
    products = Product.objects.order_by('-id')[:5]
    grouped_products = [products[n:n + 3] for n in range(0, len(products), 3)]
    return render(request, 'store/index.html',
                  {'title': 'Главная страница Lana_toys', 'products': products, 'grouped_products': grouped_products, })


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


def thank_you(request):
    return render(request, 'store/thank_you.html')


def how_to_buy(request):
    return render(request, 'store/how_to_buy.html')


def contacts(request):
    return render(request, 'store/contacts.html')


@csrf_exempt
def send_telegram_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        telegram = request.POST.get('telegram')
        message = request.POST.get('message')

        # Отправляем сообщение в Telegram
        telegram_message = f'Имя: {name}\nТелеграм-ник: {telegram}\nСообщение: {message}'

        # Делаем запрос к Telegram API для отправки сообщения
        requests.get(
            f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={settings.TELEGRAM_CHAT_ID}&text={telegram_message}')

        # После отправки сообщения, перенаправляем пользователя на другую страницу
        return render(request, 'store/thank_you.html')
