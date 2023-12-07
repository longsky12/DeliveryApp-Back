from django.urls import path

from . import views

# 다른 앱과 URL 별칭이 겹치지 않도록 app name 설정
app_name='orders'

urlpatterns = [
    path('order/',views.OrderTemplateView.as_view(),name='order'),



    path('api/order/',views.OrderListCreateView.as_view(),name='order-list-create'),
    path('api/order/<int:pk>/',views.OrderRetrieveUpdateDestroyView.as_view(),name='order-retrieve-update-destroy'),
    path('api/order/<int:pk>/update-status/',views.updateOrderStatus,name='update-order-status'),
    path('api/cart/',views.CartCreateView.as_view(), name='cart-create'),
    path('api/cart/<int:pk>/',views.CartRetrieveDestroyView.as_view(), name='cart-retrieve-update-destroy'),
    path('api/cartitem/',views.CartItemListCreateView.as_view(),name='cartitem-list-create'),
    path('api/cartitem/<int:pk>/',views.CartItemRetrieveUpdateDestroyView.as_view(),name='cartitem-retrieve-update-destroy'),

]

# GET       api/order/      주문 가져오기
# POST      api/order/      주문 생성하기
# GET       api/order/<pk>  주문 한개 가져오기
# PUT       api/order/<pk>  주문 업데이트
# DELETE    api/order/<pk>  주문 삭제 => 이 기능이 있어도 되나 판단이 안선다 아직까지는..

# POST      api/cart/       장바구니 생성!
# GET       api/cart/<pk>   장바구니 가져와서 읽기 -> cartId, userId, status만 존재
# DELETE    api/cart/<pk>   장바구니 삭제

# GET       api/cartitem/   Header에 들어있는 Token의 주인의 장바구니 전체 표시(담은 메뉴 전체 보여줌)
# POST      api/cartitem/   Cart에 들어갈 Item 생성 
# GET       api/cartitem/<pk> 장바구니에 담긴 아이템 1개의 세부사항
# PUT       api/cartitem/<pk> 업데이트 -> 수량만 업데이트 하기
# DELETE    api/cartitem/<pk> 장바구니에 담긴 아이템 1개 삭제

