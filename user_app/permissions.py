from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    message="다른 사용자의 주소는 볼 수 없습니다."

    def has_object_permission(self, request, view,obj):
        # 식당 주인들은 못봄
        if request.user.is_restaurant_admin:
            return False
        
        # 소유자만 볼 수 있음
        return obj.userId == request.user
        