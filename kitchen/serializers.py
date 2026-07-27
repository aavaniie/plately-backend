from rest_framework import serializers

from .models import KitchenTicket
from orders.models import OrderItem


class KitchenOrderItemSerializer(serializers.ModelSerializer):

    qty = serializers.IntegerField(
        source="quantity",
        read_only=True
    )

    name = serializers.CharField(
        source="food.name",
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "qty",
            "name",
            "cooking_time",
        ]


class KitchenTicketSerializer(serializers.ModelSerializer):

    order_id = serializers.CharField(
        source="order.order_id",
        read_only=True
    )

    table = serializers.IntegerField(
        source="order.table.number",
        read_only=True
    )

    items = KitchenOrderItemSerializer(
        source="order.items",
        many=True,
        read_only=True
    )

    class Meta:
        model = KitchenTicket
        fields = [
            "id",
            "order",
            "order_id",
            "table",
            "station",
            "priority",
            "status",
            "target_time",
            "note",
            "created_at",
            "items",
        ]