from django.urls import path

from . import views

# 다른 앱과 URL 별칭이 겹치지 않도록 app name 설정
app_name='orders'

urlpatterns = [
    path('', views.index),
    path('api/order/',views.OrderListCreateView.as_view(),name='order-list-create'),
    path('api/order/<int:pk>/',views.OrderRetrieveUpdateDestroyView.as_view(),name='order-retrieve-update-destroy'),
    path('api/ordermenu/',views.OrderListCreateView.as_view(),name='order-list-create'),
    path('api/ordermenu/<int:pk>/',views.OrderRetrieveUpdateDestroyView.as_view(),name='order-retrieve-update-destroy'),

]