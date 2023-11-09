from rest_framework import routers
from django.urls import path

from . import views

# 다른 앱과 URL 별칭이 겹치지 않도록 app name 설정
app_name='restaurants'


urlpatterns = [
    path('', views.index), 

    # 가게 생성 POST
    path('api/restaurants/create/', views.RestaurantCreateView.as_view(), name='restaurant-create'),
    
    # 가게 리스트 GET
    path('api/restaurants/', views.RestaurantListView.as_view(), name='restaurant-list'),
    
    # 특정 가게 상세정보 GET
    path('api/restaurants/<int:pk>/', views.RestaurantRetrieveView.as_view(), name='restaurant-detail'),
    
    # 특정 가게 업데이트(수정) PATCH
    path('api/restaurants/update/<int:pk>/', views.RestaurantUpdateView.as_view(), name='restaurant-update'),
    
    # 특정 가게 삭제 DELETE
    path('api/restaurants/delete/<int:pk>/', views.RestaurantDestroyView.as_view(), name='restaurant-delete'),
    
    #--------------------------------------------------------
    # 메뉴 생성 POST
    path('api/menu/create/',views.MenuCreateView.as_view(), name='menu-create'),

    # 전체 가계 메뉴 리스트 GET - 과연 필요한것인가
    path('api/menu/', views.MenuListView.as_view(), name='menu-list'),

    # 특정 가계 메뉴 리스트 GET
    path('api/menu/store/<int:storeId>/', views.MenuListByStoreIdView.as_view(), name='menu-list-by-store'),

    # 특정 메뉴 1개 가져오기 GET
    path('api/menu/<int:pk>/',views.MenuRetrieveView.as_view(),name='menu-detail'),

    # 특정 메뉴 업데이트(수정) PATCH
    path('api/menu/update/<int:pk>/',views.MenuUpdateView.as_view(),name='menu-update'),

    # 특정 메뉴 삭제 DELETE
    path('api/menu/delete/<int:pk>/',views.MenuDestroyView.as_view(),name='menu-delete'),

    #--------------------------------------------------------
    # 메뉴 옵션 생성 POST
    path('api/menuoption/create/', views.MenuOptionCreateView.as_view(), name='menuoption-create'),

    # 특정 메뉴의 옵션 리스트 GET
    path('api/menuoption/menu/<int:menuId>/',views.MenuOptionListByMenuIdView.as_view(), name='menuoption-list'),

    # 특정 메뉴 옵션 1개 가져오기 GET
    path('api/menuoption/<int:pk>/', views.MenuOptionRetrieveView.as_view(),name='menuoption-detail'),

    # 특정 메뉴 업데이트(수정) PATCH
    path('api/menuoption/update/<int:pk>/', views.MenuOptionUpdateView.as_view(),name='menuoption-update'),

    # 특정 메뉴 삭제 DELETE
    path('api/menuoption/delete/<int:pk>/',views.MenuOptionDestroyView.as_view(), name='menuoption-delete'),

    

]