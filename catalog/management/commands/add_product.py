from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Add test product to the database'

    def handle(self, *args, **kwargs):

        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Тестовая категория')

        products = [
            {'name': 'Тестировщик', 'description': 'Курс Тестировщик', 'price': 190000, 'category': category},
            {'name': 'Разработчик', 'description': 'Курс Разработчик', 'price': 189000, 'category': category},
            {'name': 'Аналитик', 'description': 'Курс Аналитик', 'price': 187000, 'category': category},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name} - {product.description}'))
            else:
                self.stdout.write(self.style.WARNING(f'Student already exists: {product.name} - {product.description}'))