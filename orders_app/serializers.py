from rest_framework import serializers
from .models import Order, OrderMenu

# Listing fields makes it easier to understand than using __all__.
# 필드를 나열하면 __all__을 쓴것보다 쉽게 파악할 수 있다.
class OrderMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMenu
        fields = ['menu', 'name', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    orderMenu = OrderMenuSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'userId', 'restaurantId', 'paymentMethod', 'totalPrice', 'requestMsg', 'orderTime', 'reOrderTime', 'status', 'orderMenu']
