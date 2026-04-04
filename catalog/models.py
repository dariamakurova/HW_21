from datetime import datetime

from django.db import models
from django.db.models import ForeignKey

from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    description = models.CharField(max_length=255, verbose_name="Описание")
    photo = models.ImageField(
        upload_to="products/photo", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
        blank=True,
        verbose_name="Категория"
    )
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateField(verbose_name="Дата создания", auto_now=True)
    updated_at = models.DateField(verbose_name="Дата последнего изменения", auto_now=True)
    is_published = models.CharField(verbose_name="Статус публикации", choices=[("published", "опубликован"), ("unpublished", "не опубликован")], default="не опубликован")
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
        blank=True,
        verbose_name="Владелец"
    )


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product")
        ]

    def __str__(self):
        return self.name
