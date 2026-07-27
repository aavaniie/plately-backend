from django.db import models
from authentication.models import User
import random


class Restaurant(models.Model):

    name = models.CharField(
        max_length=200
    )

    address = models.TextField()

    phone = models.CharField(
        max_length=15
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="restaurants"
    )

    opening_time = models.TimeField(
        null=True,
        blank=True
    )

    closing_time = models.TimeField(
        null=True,
        blank=True
    )

    tax_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=5
    )

    service_charge = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=10
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.name



class Table(models.Model):

    STATUS_CHOICES = [
        ("Available", "Available"),
        ("Occupied", "Occupied"),
        ("Reserved", "Reserved"),
        ("Cleaning", "Cleaning"),
    ]


    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="tables"
    )


    number = models.PositiveIntegerField()


    pin = models.CharField(
        max_length=6,
        unique=True,
        blank=True
    )


    seats = models.PositiveIntegerField(
        default=4
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Available"
    )


    class Meta:
        unique_together = (
            "restaurant",
            "number",
        )


    def save(self, *args, **kwargs):

        if not self.pin:
            self.pin = str(random.randint(100000, 999999))

        super().save(*args, **kwargs)


    def __str__(self):
        return f"Table {self.number}"