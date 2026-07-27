from rest_framework import generics
from .models import Restaurant, Table
from .serializers import RestaurantSerializer, TableSerializer


class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer



class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer



class TableListCreateView(generics.ListCreateAPIView):
    serializer_class = TableSerializer

    def get_queryset(self):
        return Table.objects.all()



class TableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer