from rest_framework import serializers
from .models import Order, Cart, CartItem

# Listing fields makes it easier to understand than using __all__.
# 필드를 나열하면 __all__을 쓴것보다 쉽게 파악할 수 있다.
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['orderId', 'storeId','userId', 'cartId', 'paymentMethod', 'totalPrice', 'requestMsg','status']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'