from django.contrib import admin
from .models import Category, FoodItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "restaurant",
    )


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "available",
        "chef_recommended",
    )

    list_filter = (
        "category",
        "available",
        "vegetarian",
        "vegan",
    )

    search_fields = (
        "name",
    )