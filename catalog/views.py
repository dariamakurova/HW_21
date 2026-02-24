from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'catalog/catalog.html')