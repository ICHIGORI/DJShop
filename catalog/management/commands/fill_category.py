import json

from django.core.management import BaseCommand
from config.settings import BASE_DIR
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        with open(BASE_DIR / "fixtures/catalog_data.json", encoding="utf-8") as file:
            content = json.load(file)
        category_list = []
        product_list = []

        for item in content:
            if item['model'] == "catalog.category":
                category_list.append(Category(**item["fields"], pk=item["pk"]))

        Category.objects.bulk_create(category_list)

        for item in content:
            if item['model'] == "catalog.product":
                item["fields"]["category"] = Category.objects.get(pk=item['fields']['category'])
                product_list.append(Product(**item["fields"], pk=item["pk"]))

        Product.objects.bulk_create(product_list)
