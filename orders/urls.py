from django.urls import path

from .views import (
    OrderListCreateView,
    OrderStatusView,
)


urlpatterns = [
    path(
        "",
        OrderListCreateView.as_view(),
        name="orders"
    ),

    path(
        "status/<str:order_id>/",
        OrderStatusView.as_view(),
        name="order-status"
    ),
]