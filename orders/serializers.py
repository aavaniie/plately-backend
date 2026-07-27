from rest_framework import serializers
from django.utils import timezone

from .models import Order, OrderItem
from restaurant.models import Table
from menu.models import FoodItem
from kitchen.models import KitchenTicket


class OrderItemSerializer(serializers.ModelSerializer):

    food_name = serializers.CharField(
        source="food.name",
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "food",
            "food_name",
            "quantity",
            "price",
            "cooking_time",
        ]


class CreateOrderItemSerializer(serializers.Serializer):

    food = serializers.IntegerField()
    quantity = serializers.IntegerField(
        min_value=1
    )


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(
        many=True,
        read_only=True
    )

    create_items = CreateOrderItemSerializer(
        many=True,
        write_only=True
    )

    table = serializers.IntegerField(
        write_only=True
    )

    class Meta:
        model = Order

        fields = [
            "id",
            "order_id",
            "restaurant",
            "customer",
            "table",
            "status",
            "note",
            "total",
            "created_at",
            "items",
            "create_items",
        ]

        read_only_fields = [
            "id",
            "order_id",
            "restaurant",
            "customer",
            "status",
            "total",
            "created_at",
            "items",
        ]

    def create(self, validated_data):

        table_number = validated_data.pop("table")
        create_items = validated_data.pop("create_items")
        note = validated_data.pop("note", "")

        table = Table.objects.get(
            number=table_number
        )

        order = Order.objects.create(
            restaurant=table.restaurant,
            table=table,
            order_id=f"ORD{timezone.now().strftime('%Y%m%d%H%M%S')}",
            status="Received",
            note=note
        )

        total = 0
        max_time = 0

        for item in create_items:

            food = FoodItem.objects.get(
                id=item["food"]
            )

            OrderItem.objects.create(
                order=order,
                food=food,
                quantity=item["quantity"],
                price=food.price,
                cooking_time=food.cooking_time
            )

            total += food.price * item["quantity"]

            max_time = max(
                max_time,
                food.cooking_time
            )

        order.total = total
        order.save()

        KitchenTicket.objects.create(
            order=order,
            station="Grill",
            priority="normal",
            status="Incoming",
            target_time=max_time,
            note=order.note
        )

        return order