from rest_framework import permissions

class IsRestaurantOwnerPermission(permissions.BasePermission):
    message="해당 식당 관리자만 주문을 읽을 수 있습니다."

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and(request.user.is_restaurant_admin and obj.storeId.userId==request.user)
    

class AdminPermission(permissions.BasePermission):
    message="식당 관리자는 주문을 읽을수만 있습니다."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_restaurant_admin
    
    # 관리자 삭제 가능
    def has_object_permission(self, request, view, obj):
        return request.user.is_restaurant_admin and (request.method in permissions.SAFE_METHODS)

class UserPermission(permissions.BasePermission):
    message = "사용자는 다른 사람의 주문을 읽을 수 없습니다."
    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_restaurant_admin
    
    # 사용자 읽기만 가능
    def has_object_permission(self, request, view, obj):
        return not request.user.is_restaurant_admin and (request.method in permissions.SAFE_METHODS)