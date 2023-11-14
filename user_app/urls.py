from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# 다른 앱과 URL 별칭이 겹치지 않도록 app name 설정
app_name='user'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name ='register' ),
    path('login/',views.LoginView.as_view(),name = 'login'),

    # 나중에 csrf 토큰 필요시 활성화
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # csrf 토큰이 필요없는 로그아웃 실제 서비스시 사용 X GET
    path('logout/',views.CustomLogoutView.as_view(),name='logout'),
]