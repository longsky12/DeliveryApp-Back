from django.db import models
from django.utils import timezone

class Order(models.Model):
    class PaymentMethodList(models.TextChoices):
        CASH = 'CASH', '현금'
        CREDIT_CARD = 'CREDIT_CARD', '신용카드'
        KAKAO_PAY = 'KAKAO_PAY', '카카오페이'
    
    class OrderStatusList(models.TextChoices):
        ACCEPTING_ORDER = 'ACCEPTING_ORDER', '주문 접수 중'
        ORDER_COMPLETE = 'ORDER_COMPLETE', '주문 완료'
        DELIVERY = 'DELIVERY', '배달 중'
        DELIVERY_COMPLETE = 'DELIVERY_COMPLETE', '배달 완료'

    userId = models.ForeignKey('user_app.CustomUser',on_delete=models.CASCADE)
    restaurantId = models.ForeignKey('restaurants_app.Restaurant',on_delete=models.CASCADE, related_name='order')

    paymentMethod = models.CharField(max_length=20,choices=PaymentMethodList.choices)
    totalPrice = models.PositiveIntegerField()
    requestMsg = models.CharField(max_length=255,default="(없음)")
    orderTime = models.DateTimeField(auto_now_add=True)     # createdDate
    reOrderTime = models.DateTimeField(auto_now=True)       # modifiedDate
    status = models.CharField(max_length=255,choices=OrderStatusList.choices,default=OrderStatusList.ACCEPTING_ORDER)

class OrderMenu(models.Model):
    menu = models.ForeignKey('restaurants_app.Menu',on_delete=models.CASCADE)
    order = models.ForeignKey('Order',on_delete=models.CASCADE,related_name='orderMenu')
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

