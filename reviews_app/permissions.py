
from rest_framework import permissions
from .models import Reviews


class IsOrderFromRestaurant(permissions.BasePermission):
    message = "Only customers who have ordered from this restaurant can leave a review."

    def has_object_permission(self, request, view, obj):
        user = request.user
        
        # obj가 리뷰 모델일 경우
        if isinstance(obj,Reviews):
            reviewAuthor = obj.userId
            restaurant = obj.storeId
            
            if user.is_restaurant_admin:
                return False
            
            return user==reviewAuthor and user.orders.filter(restaurant=restaurant).exists()
        
        return False
