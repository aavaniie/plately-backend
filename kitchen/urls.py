from django.urls import path

from .views import (
    KitchenTicketListView,
    KitchenTicketUpdateView,
)


urlpatterns = [

    path(
        "",
        KitchenTicketListView.as_view(),
        name="kitchen-tickets"
    ),

    path(
        "<int:pk>/",
        KitchenTicketUpdateView.as_view(),
        name="kitchen-ticket-update"
    ),
]