from django.db import models
from orders.models import Order


class KitchenTicket(models.Model):

    STATUS_CHOICES = [
        ("Incoming", "Incoming"),
        ("Preparing", "Preparing"),
        ("Ready", "Ready"),
        ("Completed", "Completed"),
    ]


    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="kitchen_ticket"
    )


    station = models.CharField(
        max_length=50
    )


    priority = models.CharField(
        max_length=20,
        choices=[
            ("normal", "Normal"),
            ("high", "High"),
        ],
        default="normal"
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Incoming"
    )


    target_time = models.PositiveIntegerField(
        default=0
    )


    note = models.TextField(
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.order.order_id} Ticket"