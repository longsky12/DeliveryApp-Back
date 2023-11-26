# DeliveryApp-Back

11.03.Fri

1. use kakaopayment api
2. add bootstrap.min.css, payment_secrets.json
3. config/my_settings.py -> make get_ADMIN_KEY() function
   ㄴADMIN_KEY is like a SECRETKEY
4. Add four html files -> but i have to use rest api


***요청을 보낼시 각 요청마다 필요한 Json 형식의 Body***

# CustomUser Model  
POST  http://localhost:8000/register/  
{  
    "username":"익명",  
    "password":"1234",  
    "password2":"1234",  
    "email":"1@naver.com",  
    "is_restaurant_admin":"False"  
}  

POST  http://localhost:8000/login/  
{  
    "username":"익명",  
    "password":"1234"  
}  

GET  http://localhost:8000/logout/  
GET  http://localhost:8000/user/ => 전체 유저 리스트  

=================================================================================  

# Address Model  
GET  http://localhost:8000/api/address/  => 헤더에 있는 토큰 주인의 전체 주소 목록 반환  
POST  http://localhost:8000/api/address/ => 생성  
{  
    "address":"서울"  
}  

GET  http://localhost:8000/api/address/<pk>/ => 주소 Id에 해당하는 주소 한개 반환  
PUT  http://localhost:8000/api/address/<pk>/ => 주소 Id에 해당하는 주소 변경  
{  
    "address":"서울"  
}  

DELETE  http://localhost:8000/api/address/<pk>/ => 주소 Id에 해당하는 주소 삭제  

=================================================================================  

# Restaurant Model  
GET    api/restaurants/:         모든 레스토랑 리스트를 가져옴  
POST   api/restaurants/:         새로운 레스토랑을 생성함  
GET    api/restaurants/{id}/:    특정 레스토랑의 세부 정보를 가져옴  
PUT    api/restaurants/{id}/:    특정 레스토랑을 수정함  
DELETE api/restaurants/{id}/:    특정 레스토랑을 삭제함  

Restaurant 생성시  
{  
  "name": "식당",  
  "category": "1",  
  "address": "서울시 강남구",  
  "phone": "010-1234-5678",  
  "content": "맛있는 음식을 제공합니다.",  
  "minDeliveryPrice": "15000",  
  "deliveryTip": "2000",  
  "minDeliveryTime": "30",  
  "maxDeliveryTime": "60",  
  "rating": "4.5",  
  "dibsCount": "100",  
  "reviewCount": "50",  
  "operationHours": "10:00 - 22:00",  
  "closedDays": "월요일",  
  "deliveryAddress": "서울시 강남구"  
}  

# MENU  
POST    api/restaurants/{restaurant_id}/menus/              메뉴 생성(Create Menu)  
GET     api/restaurants/{restaurant_id}/menus/              특정 레스토랑의 모든 메뉴 조회  
GET     api/restaurants/{restaurant_id}/menus/{menu_id}/    특정 레스토랑의 특정 메뉴 조회  
PUT     api/restaurants/{restaurant_id}/menus/{menu_id}/    특정 레스토랑의 특정 메뉴 수정  
PATCH   api/restaurants/{restaurant_id}/menus/{menu_id}/    특정 레스토랑의 특정 메뉴 일부 수정  
DELETE  api/restaurants/{restaurant_id}/menus/{menu_id}/    특정 레스토랑의 특정 메뉴 삭제  

Menu 생성시  
{  
    "category":"분식",  
    "name":"떡볶이",  
    "price":"2000"   
}  


# MENUOPTION  
GET       /api/menus/{menu_id}/menu-options/                  특정 메뉴의 메뉴 옵션 리스트 조회  
POST      /api/menus/{menu_id}/menu-options/                  메뉴옵션 생성  
GET       /api/menus/{menu_id}/menu-options/{menu_option_id}/ 특정 메뉴의 메뉴 옵션 조회  
PUT       /api/menus/{menu_id}/menu-options/{menu_option_id}/ 특정 메뉴의 메뉴 옵션 수정(전부+일부)  
DELETE    /api/menus/{menu_id}/menu-options/{menu_option_id}/ 특정 메뉴의 메뉴 옵션 삭제  

MenuOption 생성시  
{  
    "option":"option1",  
    "content":"content1",  
    "price":"1000"  
}  

=================================================================================  

# Order  
GET    api/order/         생성한 주문 조회(주문 받은 레스토랑 사장님 & 주문한 사람 확인 가능)  
POST   api/order/         주문 생성(사장님이 아닌 계정으로 로그인시 주문 생성 가능)  

Order 생성시  
{  
    "storeId":"2",  
    "paymentMethod":"card",  
    "totalPrice":"150000",  
    "requestMsg":"빨리 보내주세요"  
}  

GET    api/order/<pk>/    생성한 주문 조회(해당 pk값의 본인 주문 조회)  
DELETE api/order/<pk>/    주문 받은 레스토랑의 사장님이 삭제 가능  


