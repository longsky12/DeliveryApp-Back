from django.urls import path

from . import views

# 다른 앱과 URL 별칭이 겹치지 않도록 app name 설정
app_name='user'

urlpatterns = [
    path('', views.index),
    path('create/', views.create_user, name='create_user'),
    path('list/',views.user_list, name='user_list'),
]