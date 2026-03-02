from django.urls import path
from catalog import views
from catalog.views import index, product_info, ProductListView

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('category_1/', views.category_1, name='category_1'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('products/<int:pk>/', views.product_info, name='product_info'),
    path('', index),
]