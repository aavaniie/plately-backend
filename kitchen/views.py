from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import KitchenTicket
from .serializers import KitchenTicketSerializer


class KitchenTicketListView(generics.ListAPIView):

    serializer_class = KitchenTicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            KitchenTicket.objects
            .select_related(
                "order",
                "order__table"
            )
            .order_by("-created_at")
        )


class KitchenTicketUpdateView(generics.RetrieveUpdateAPIView):

    queryset = KitchenTicket.objects.all()
    serializer_class = KitchenTicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):

        ticket = serializer.save()

        status_map = {
            "Incoming": "Received",
            "Preparing": "Preparing",
            "Ready": "Ready",
            "Completed": "Completed",
        }

        if ticket.status in status_map:

            ticket.order.status = status_map[
                ticket.status
            ]

            ticket.order.save(
                update_fields=[
                    "status"
                ]
            )