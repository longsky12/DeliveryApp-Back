from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .models import Order
from .serializers import OrderSerializer
from .permissions import AdminPermission, UserPermission, IsRestaurantOwnerPermission

# Order
# CreateAPIView only create : POST
# ListCreateAPIView create & list : POST & GET
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def get_permissions(self):
        if self.request.user.is_restaurant_admin:
            permission_class = [AdminPermission]
        else:
            permission_class = [UserPermission]
        return [permission() for permission in permission_class]
    
    def create(self,request,*args,**kwargs):
        if not request.user.is_restaurant_admin:
            token = request.headers.get('Authorization').split(' ')[1]
            try:
                authorizedToken = Token.objects.get(key=token)
                user = authorizedToken.user
                userId = user.pk
                request.data['userId']=userId
            except Token.DoesNotExist:
                return Response({"message":"Invalid token"},status=status.HTTP_401_UNAUTHORIZED)
            except Exception as e:
                return Response({"message":f"An error occured:{str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message":"식당 관리자 계정으로는 주문할 수 없습니다."},status=status.HTTP_403_FORBIDDEN)
        return super().create(request,*args,**kwargs)


# RetrieveUpdateDestroyAPIView : POST, PATCH, DELETE
class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.request.user.is_restaurant_admin:
            permission_class=[IsRestaurantOwnerPermission]
        else:
            permission_class=[UserPermission]
        return [permission() for permission in permission_class]

