from rest_framework import serializers
from .models import Restaurant, Table


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = "__all__"



class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = "__all__"