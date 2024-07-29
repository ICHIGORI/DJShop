from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price_purchase")
    list_filter = ("name", "category", "price_purchase", "description")
    search_fields = ("name", "category")
