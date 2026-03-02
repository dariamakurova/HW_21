from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

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

def catalog(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/catalog.html', context)

def index(request):
    return render(request, 'catalog/base.html')

def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product" : product}
    return render(request, 'catalog/product_info.html', context)