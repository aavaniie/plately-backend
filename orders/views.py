from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer


class OrderListCreateView(generics.ListCreateAPIView):

    serializer_class = OrderSerializer


    def get_permissions(self):

        if self.request.method == "POST":
            return [AllowAny()]

        return [IsAuthenticated()]


    def get_queryset(self):

        return (
            Order.objects
            .filter(
                restaurant__isnull=False
            )
            .prefetch_related(
                "items"
            )
            .order_by(
                "-created_at"
            )
        )


    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data
        )

        if not serializer.is_valid():
            print(serializer.errors)

            return Response(
                serializer.errors,
                status=400
            )


        order = serializer.save()


        return Response(
            OrderSerializer(order).data,
            status=status.HTTP_201_CREATED
        )



class OrderStatusView(APIView):

    permission_classes = [AllowAny]


    def get(self, request, order_id):

        try:

            order = Order.objects.get(
                order_id=order_id
            )

        except Order.DoesNotExist:

            return Response(
                {
                    "error": "Order not found"
                },
                status=404
            )


        return Response(
            {
                "order_id": order.order_id,
                "status": order.status,
            }
        )