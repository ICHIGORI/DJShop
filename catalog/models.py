from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category", help_text="Введите название категории")
    description = models.TextField(max_length=250, verbose_name="Description", help_text="Опишите продукт")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Product", help_text="Введите название продукта")
    description = models.TextField(max_length=250, verbose_name="Description", help_text="Опишите продукт")
    preview_image = models.ImageField(upload_to='product/preview_img/', verbose_name="PreviewImg", **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_purchase = models.FloatField(verbose_name="PricePurchase", help_text="Цена продукта")
    created_at = models.DateField(help_text="Дата создания")
    updated_at = models.DateField(help_text="Дата обновления")

    def __str__(self):
        return f"{self.category=} {self.name=} ({self.price_purchase} {self.created_at=} {self.updated_at=})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ('name', 'category', 'price_purchase', 'created_at', 'updated_at',)
