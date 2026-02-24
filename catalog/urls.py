from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('category_1/', views.category_1, name='category_1'),
    path('catalog/', views.catalog, name='catalog'),
]