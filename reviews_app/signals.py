from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Reviews

@receiver(pre_save, sender=Reviews)
def check_order_before_review(sender, instance, **kwargs):
    if instance.userId:  # 유저 정보가 존재하는지 확인
        user_orders = instance.userId.order_set.filter(status='배달 완료')
        if not user_orders.exists():
            raise ValidationError("주문을 완료한 후에 리뷰를 작성할 수 있습니다.")
