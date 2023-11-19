from rest_framework import routers
from django.urls import path, include

from . import views

# 다른 앱과 URL 별칭이 겹치지 않도록 app name 설정
app_name='restaurants'

router = routers.DefaultRouter()
router.register(r'restaurants',views.RestaurantViewSet, basename='restaurants')
router.register(r'restaurants/(?P<restaurant_id>\d+)/menus',views.MenuViewSet, basename='menus')
router.register(r'menus/(?P<menu_id>\d+)/menu-options',views.MenuOptionViewSet,basename='menu-options')

urlpatterns = [
    path('', views.index), 
    path('api/',include(router.urls)),
]

# RESTAURANT
# GET    /restaurants/:         모든 레스토랑 리스트를 가져옴
# POST   /restaurants/:         새로운 레스토랑을 생성함
# GET    /restaurants/{id}/:    특정 레스토랑의 세부 정보를 가져옴
# PUT    /restaurants/{id}/:    특정 레스토랑을 수정함
# DELETE /restaurants/{id}/:    특정 레스토랑을 삭제함

# MENU
# POST    /restaurants/{restaurant_id}/menus/              메뉴 생성(Create Menu)
# GET     /restaurants/{restaurant_id}/menus/              특정 레스토랑의 모든 메뉴 조회
# GET     /restaurants/{restaurant_id}/menus/{menu_id}/    특정 레스토랑의 특정 메뉴 조회
# PUT     /restaurants/{restaurant_id}/menus/{menu_id}/    특정 레스토랑의 특정 메뉴 수정
# PATCH   /restaurants/{restaurant_id}/menus/{menu_id}/    특정 레스토랑의 특정 메뉴 일부 수정
# DELETE  /restaurants/{restaurant_id}/menus/{menu_id}/    특정 레스토랑의 특정 메뉴 삭제

# MENUOPTION


"""
    # viewSet 사용 이전 genericView & APIView 사용시

    # 가게 생성 POST
    path('api/restaurant/create/', views.RestaurantCreateView.as_view(), name='restaurant-create'),
    
    # 가게 리스트 GET
    path('api/restaurant/', views.RestaurantListView.as_view(), name='restaurant-list'),
    
    # 특정 가게 상세정보 GET
    path('api/restaurant/<int:pk>/', views.RestaurantRetrieveView.as_view(), name='restaurant-detail'),
    
    # 특정 가게 업데이트(수정) PATCH
    path('api/restaurant/update/<int:pk>/', views.RestaurantUpdateView.as_view(), name='restaurant-update'),
    
    # 특정 가게 삭제 DELETE
    path('api/restaurant/delete/<int:pk>/', views.RestaurantDestroyView.as_view(), name='restaurant-delete'),

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
"""