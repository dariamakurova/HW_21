from django.urls import path
from django.views.decorators.cache import cache_page

from catalog import views
from catalog.models import Product
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductListViewByCategory, CategoryListView
from users.apps import UsersConfig

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('category_1/', views.category_1, name='category_1'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_info'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/<int:pk>/', ProductListViewByCategory.as_view(), name='products_by_category'),
    path('categories/', CategoryListView.as_view(), name='categories')
]