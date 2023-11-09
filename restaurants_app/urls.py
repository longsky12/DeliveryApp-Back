from rest_framework import routers
from django.urls import path

from . import views

# 다른 앱과 URL 별칭이 겹치지 않도록 app name 설정
app_name='restaurants'


urlpatterns = [
    path('', views.index),
    path('api/restaurants/create/', views.RestaurantCreateView.as_view(), name='restaurant-create'),
    path('api/restaurants/', views.RestaurantListView.as_view(), name='restaurant-list'),
    path('api/restaurants/<int:pk>/', views.RestaurantRetrieveView.as_view(), name='restaurant-detail'),
    path('api/restaurants/update/<int:pk>/', views.RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('api/restaurants/delete/<int:pk>/', views.RestaurantDestroyView.as_view(), name='restaurant-delete'),
]