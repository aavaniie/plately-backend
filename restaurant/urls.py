from django.urls import path
from .views import (
    RestaurantListCreateView,
    RestaurantDetailView,
    TableListCreateView,
    TableDetailView,
)


urlpatterns = [

    # Restaurant
    path(
        "restaurants/",
        RestaurantListCreateView.as_view(),
        name="restaurant-list"
    ),

    path(
        "restaurants/<int:pk>/",
        RestaurantDetailView.as_view(),
        name="restaurant-detail"
    ),


    # Tables
    path(
        "tables/",
        TableListCreateView.as_view(),
        name="table-list"
    ),

    path(
        "tables/<int:pk>/",
        TableDetailView.as_view(),
        name="table-detail"
    ),
]