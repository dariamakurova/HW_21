from django.contrib import admin

from blog.models import Article


# Register your models here.
@admin.register(Article)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "body", "preview", "created_at", "is_published", "views_count")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "body")