from django.contrib import admin
from .models import KitchenTicket


@admin.register(KitchenTicket)
class KitchenTicketAdmin(admin.ModelAdmin):

    list_display = (
        "order",
        "station",
        "status",
        "priority",
        "created_at",
    )

    list_filter = (
        "status",
        "station",
        "priority",
    )

    search_fields = (
        "order__order_id",
    )