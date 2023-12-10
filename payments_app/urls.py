from django.urls import path

from . import views


# 다른 앱과 URL 별칭이 겹치지 않도록 app name 설정
app_name = 'payments'

urlpatterns = [
    path('kakaopay/', views.kakaoPay, name='kakaopay'),
    path('kakaopaylogic/',views.kakaoPayLogic, name='kakaopaylogic'),
    path('paysuccess/', views.paySuccess, name='paysuccess'),
    path('payfail/', views.payFail, name='payfail'),
    path('paycancel/', views.payCancel, name='paycancel'),
    
    # path('api/payment/',views.PaymentViewSet.as_view({'post':'create'}),name='payment-create'),
    # path('api/payment/approval/',views.PaymentApprovalViewSet.as_view({'post':'create'}),name='payment-approve'),

    path('index/',views.index),
    path('toss_pay/',views.window, name='toss_pay'),
    path('toss_pay_success/',views.success, name='toss_pay_success'),
    path('fail/',views.fail, name='toss_pay_fail'),
]