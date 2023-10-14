from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,name,currentAddress,phone,password=None):
        if not name:
            raise ValueError('must have user name')
        user = self.model(
            name=name,
            currentAddress = currentAddress,
            phone = phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,name,currentAddress,phone,password=None):
        user = self.create_user(name,currentAddress,phone,password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    currentAddress = models.CharField(max_length=255)
    phone = models.CharField(max_length=11,unique=True)
    createDate = models.DateTimeField(default=timezone.now) # 생성 일시
    modifiedDate = models.DateTimeField(auto_now=True) # 수정 일시(모델 저장시 자동으로 현재시간 설정)

    # django의 필수 field is_active & is_admin
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name','currentAddress',]

    def __str__(self):
        return self.name

    # 커스텀 유저 모델을 기본 유저 모델로 사용하기 위해 구현할 부분
    # 권한이 있음을 알림, Object를 반환하는 경우 해당 Object로 사용 권한 확인 절차 필요
    def has_perm(self,perm, obj=None):
        return True

    # 주어진 App의 model에 접근 가능하도록 함
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

