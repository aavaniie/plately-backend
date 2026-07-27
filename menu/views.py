from rest_framework import generics, permissions
from .models import Category, FoodItem
from .serializers import (
    CategorySerializer,
    FoodItemSerializer,
)


class CategoryListView(generics.ListAPIView):

    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Category.objects.all()


class FoodListCreateView(generics.ListCreateAPIView):

    serializer_class = FoodItemSerializer

    def get_queryset(self):
        return FoodItem.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class FoodDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]