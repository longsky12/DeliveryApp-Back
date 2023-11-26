from rest_framework import serializers
from .models import Order

# Listing fields makes it easier to understand than using __all__.
# 필드를 나열하면 __all__을 쓴것보다 쉽게 파악할 수 있다.
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['orderId', 'storeId','userId', 'paymentMethod', 'totalPrice', 'requestMsg']

