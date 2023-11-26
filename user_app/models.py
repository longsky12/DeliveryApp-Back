from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    is_restaurant_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')


class Address(models.Model):
    addressId = models.BigAutoField(primary_key=True)
    userId = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255,default='일반')

    def __str__(self):
        return f"{self.addressId} - {self.address}"