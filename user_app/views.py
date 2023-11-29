# TEST 용도
from django.http import JsonResponse
from django.views import View

from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from.serializers import RegisterSerializer, LoginSerializer, CustomUserSerializer, AddressSerializer
from .models import CustomUser, Address
from .permissions import UserPermission

# POST
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    # 아래 두개 추가 -> 회원가입 하려고 하는 사람은 토큰을 발급받기 전이라
    # 모든 사용자가 엔드포인트에 접근 가능하게 AllowAny로 선언
    authentication_classes = []
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(is_restaurant_admin=self.request.data.get('is_restaurant_admin',False))
        # token, created = Token.objects.get_or_create(user=user)
        # return Response({'token':token.key})
    
# POST
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        print(serializer)
        token = serializer.validated_data
        return Response({"token":token.key,"id":user.id,"ceo":user.is_restaurant_admin}, status = status.HTTP_200_OK)


    
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views

# GET
class CustomLogoutView(auth_views.LogoutView):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
# Test 용도
class CustomUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
# ============================================================
# Address List Create View
class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes = [UserPermission]

    def get_queryset(self):
        user = self.request.user
        return Address.objects.filter(userId=user)
    
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
            return Response({"message":"식당 관리자 계정으로는 주소를 추가 할 수 없습니다."},status=status.HTTP_403_FORBIDDEN)
        return super().create(request,*args,**kwargs)

# ============================================================
# Address Retrieve Update Destroy View
class AddressRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[UserPermission]

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"message": "주소가 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)