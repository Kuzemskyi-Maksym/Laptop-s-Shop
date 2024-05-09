from django.contrib import admin
from .models import Product


# Модель Product
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("name", "price")  # Виправлення: видалено неіснуючі поля
    search_fields = ("name",)  # Виправлення: видалено категорію
    # Виправлення: видалено фільтрування за категорією
    ordering = ("name", "price")
    list_per_page = 20
    # Виправлення: видалено неіснуюче поле з list_editable


admin.site.register(Product, ProductModelAdmin)
