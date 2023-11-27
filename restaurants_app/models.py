from django.db import models
from django.contrib.auth import get_user_model
class Restaurant(models.Model):
    storeId = models.BigAutoField(primary_key=True)
    userId = models.ForeignKey('user_app.CustomUser',related_name='restaurant',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.SmallIntegerField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    content = models.CharField(max_length=255,blank=True,null=True)
    minDeliveryPrice = models.IntegerField()
    deliveryTip = models.IntegerField(default=0)    
    minDeliveryTime = models.IntegerField(blank=True, null=True)
    maxDeliveryTime = models.IntegerField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    dibsCount = models.IntegerField(default=0)
    reviewCount = models.IntegerField(default=0)
    operationHours = models.CharField(max_length=255, blank=True, null=True)
    closedDays = models.CharField(max_length=255, blank=True, null=True)
    deliveryAddress = models.CharField(max_length=255, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default="일반")

    def __str__(self):
        return self.name

class Menu(models.Model):
    # 메뉴 ID, PK
    menuId = models.BigAutoField(primary_key=True)
    # 외래키로 가게 ID 연결
    storeId = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    menuPictureUrl = models.TextField(blank=True, null=True)
    popularity = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default="일반")

    def __str__(self):
        return self.name


class MenuOption(models.Model):
    # 메뉴 옵션 ID, PK
    menuOptionId = models.BigAutoField(primary_key=True)
    # 외래키로 메뉴 ID 연결
    menuId = models.ForeignKey(Menu, on_delete=models.CASCADE)
    # 옵션 이름
    option = models.CharField(max_length=255)
    # 옵션 내용
    content = models.CharField(max_length=255)
    # 옵션 가격
    price = models.IntegerField()
    # 생성일
    createdDate = models.DateTimeField(auto_now_add=True)
    # 수정일
    modifiedDate = models.DateTimeField(auto_now=True)
    # 상태
    status = models.CharField(max_length=255, default="일반")

    def __str__(self):
        return self.option
    

class Dib(models.Model):
    userId = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    storeId = models.ForeignKey('Restaurant',on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255,default='일반')

    class Meta:
        unique_together = [['userId','storeId']]