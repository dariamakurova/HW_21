from gettext import Catalog

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from catalog.models import Product


def home(request):
    return render(request, 'catalog/main.html')


def contacts(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено. Мы скоро с вами свяжемся.")
    return render(request, 'catalog/contacts.html')

def category_1(request):
    return render(request, 'catalog/category_1.html')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
