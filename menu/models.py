from django.db import models
from restaurant.models import Restaurant


class Category(models.Model):

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="categories"
    )

    name = models.CharField(
        max_length=100
    )


    def __str__(self):
        return self.name



class FoodItem(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="foods"
    )


    name = models.CharField(
        max_length=150
    )


    description = models.TextField(
        blank=True
    )


    ingredients = models.JSONField(
        default=list
    )


    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )


    cooking_time = models.PositiveIntegerField(
        default=10
    )


    image = models.URLField(
        blank=True
    )


    vegetarian = models.BooleanField(
        default=False
    )


    vegan = models.BooleanField(
        default=False
    )


    salad = models.BooleanField(
        default=False
    )


    chef_recommended = models.BooleanField(
        default=False
    )


    available = models.BooleanField(
        default=True
    )


    popularity = models.IntegerField(
        default=0
    )


    def __str__(self):
        return self.name