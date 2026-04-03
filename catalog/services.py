from django.core.cache import cache
from django.db import models

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Получает данные о продуктах из кэша. Если кэш пуст, получает данные из БД."""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


class ProductService():

    @staticmethod
    def get_products_by_category(category_id):
        products = Product.objects.filter(category_id=category_id)
        if not products:
            return None
        return products

