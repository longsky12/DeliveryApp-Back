from django.db import models

class Order(models.Model):
    orderId = models.BigAutoField(primary_key=True)
    storeId = models.ForeignKey('restaurants_app.Restaurant',on_delete=models.CASCADE, related_name='order')
    userId = models.ForeignKey('user_app.CustomUser',on_delete=models.CASCADE)

    paymentMethod = models.CharField(max_length=255)
    totalPrice = models.PositiveIntegerField()
    requestMsg = models.CharField(max_length=255,default="(없음)")
    status = models.CharField(max_length=255,default='정상')

    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order ID: {self.orderId} - Store: {self.storeId} - User: {self.userId}"