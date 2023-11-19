from rest_framework import permissions

class IsRestaurantAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # 로그인 한 사용자 이며, is_restaurant_admin이 True 일 때 True 반환
        return request.user.is_authenticated and request.user.is_restaurant_admin
    
class CustomListRetrievePermission(permissions.BasePermission):
    def has_permission(self,request,view):
        return True
    
class IsOwnerOrReadOnly(permissions.BasePermission):
    # 전체 권한 처리 has_permission
    
    # 개별 권한 처리
    def has_object_permission(self, request, view, obj):
        # 읽기 권한 모든 요청에 대해 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # 가게 주인만 메뉴 or 메뉴 옵션 생성, 수정, 삭제 가능
        return obj.storeId.userId == request.user
    
class IsOwnerOrReadOnlyOption(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        menu = obj.menuId

        return menu.storeId.userId == request.user