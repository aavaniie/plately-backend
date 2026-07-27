from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "order_id",
        "restaurant",
        "table",
        "status",
        "total",
        "created_at",
    )

    list_filter = (
        "status",
        "restaurant",
    )

    search_fields = (
        "order_id",
    )

    inlines = [
        OrderItemInline,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = (
        "order",
        "food",
        "quantity",
        "price",
    )