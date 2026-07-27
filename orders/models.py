from django.db import models
from authentication.models import User
from restaurant.models import Restaurant, Table
from menu.models import FoodItem


class Order(models.Model):

    STATUS_CHOICES = [
        ("Received", "Received"),
        ("Preparing", "Preparing"),
        ("Cooking", "Cooking"),
        ("Ready", "Ready"),
        ("Completed", "Completed"),
    ]

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="orders",
        null=True,
        blank=True
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )

    table = models.ForeignKey(
        Table,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )

    order_id = models.CharField(
        max_length=30,
        unique=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Received"
    )

    note = models.TextField(
        blank=True
    )

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.order_id


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    food = models.ForeignKey(
        FoodItem,
        on_delete=models.SET_NULL,
        null=True
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    cooking_time = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.food} x {self.quantity}"