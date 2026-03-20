from django.urls import path
from catalog import views
from catalog.views import ProductListView, ProductDetailView, ContactsView

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('category_1/', views.category_1, name='category_1'),
    path('', ProductListView.as_view(), name='catalog'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
]