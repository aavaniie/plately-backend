from django.urls import path
from .views import (
    CategoryListView,
    FoodListCreateView,
    FoodDetailView,
)


urlpatterns = [

    path(
        "categories/",
        CategoryListView.as_view(),
        name="categories"
    ),

    path(
        "foods/",
        FoodListCreateView.as_view(),
        name="foods"
    ),

    path(
        "foods/<int:pk>/",
        FoodDetailView.as_view(),
        name="food-detail"
    ),

]