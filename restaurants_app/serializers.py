from rest_framework import serializers
from .models import Restaurant, Menu, MenuOption, Dib

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuOption
        fields = '__all__'

class DibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dib
        fields = ['dibId','userId','storeId','status']