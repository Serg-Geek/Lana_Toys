from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('catalog', views.catalog, name='catalog'),
    path('thank_you', views.thank_you, name='thank_you'),
    path('how_to_buy', views.how_to_buy, name='how_to_buy'),
    path('contacts', views.contacts, name='contacts'),
    path('send_telegram_message/', views.send_telegram_message, name='send_telegram_message'),
]