# TEST 용도
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View

from rest_framework import generics, status, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.authtoken.models import Token

from .serializers import RegisterSerializer, LoginSerializer, CustomUserSerializer, AddressSerializer, RewardSerializer
from .models import CustomUser, Address, Reward
from .permissions import UserPermission

from rest_framework.renderers import TemplateHTMLRenderer

# POST


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    # 아래 두개 추가 -> 회원가입 하려고 하는 사람은 토큰을 발급받기 전이라
    # 모든 사용자가 엔드포인트에 접근 가능하게 AllowAny로 선언
    authentication_classes = []
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(is_restaurant_admin=self.request.data.get(
            'is_restaurant_admin', False))
        # token, created = Token.objects.get_or_create(user=user)
        # return Response({'token':token.key})

# POST


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        token = serializer.validated_data
        return Response({"token": token.key, "id": user.id, "ceo": user.is_restaurant_admin}, status=status.HTTP_200_OK)


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
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/address.html'
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get_queryset(self):
        user = self.request.user
        return Address.objects.filter(userId=user)

    def create(self, request, *args, **kwargs):
        try:
            authorized_token = request.auth
            user = CustomUser.objects.get(id=authorized_token.user_id)
            user_id = user.pk
            request.data['userId'] = user_id

            # 요청 데이터에서 주소 관련 데이터를 추출합니다.
            detail_address = request.data.get('detail_address', '')
            road_address = request.data.get('road_address', '')

            # detail_address와 road_address를 결합하여 address 필드에 저장합니다.
            request.data['address'] = f"{road_address} {detail_address}"

            # 상위 클래스의 create 메서드를 호출하여 실제 저장 작업을 수행합니다.
            response = super().create(request, *args, **kwargs)

            # 수정: 딕셔너리 형태로 응답합니다.
            return Response({'message': '주소가 성공적으로 저장되었습니다.', 'data': response.data}, status=response.status_code)
        except CustomUser.DoesNotExist:
            return Response({"message": "사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f"오류가 발생했습니다: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data})
# ============================================================
# Address Retrieve Update Destroy View


class AddressRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"message": "주소가 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


# ============================================================
# Reward Create View
class RewardCreateView(generics.CreateAPIView):
    serializer_class = RewardSerializer
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        token = request.headers.get('Authorization').split(' ')[1]
        try:
            authorizedToken = Token.objects.get(key=token)
            user = authorizedToken.user

            existing_model = Reward.objects.filter(userId=user.pk).exists()
            if existing_model:
                return Response({"message": "이미 리워드를 개설했습니다."}, status=status.HTTP_400_BAD_REQUEST)

            if user.is_authenticated and user.is_restaurant_admin:
                return Response({"message": "사장님 계정으로는 Reward 모델을 만들 수 없습니다."}, status=status.HTTP_403_FORBIDDEN)

            userId = user.pk
            request.data['userId'] = userId

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Token.DoesNotExist:
            return Response({"message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"message": f"An error occured:{str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ============================================================
# Reward Retrieve Update Destroy View
class RewardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RewardSerializer
    queryset = Reward.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def income_points(self, instance, income):
        instance.reward += int(income)
        instance.save()

    def outcome_points(self, instance, outcome):
        if instance.reward >= int(outcome):
            instance.reward -= int(outcome)
            instance.save()
            return True
        return False

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        operation = request.data.get('operation')
        points = request.data.get('points')

        if operation == 'income':
            self.income_points(instance, points)
        elif operation == 'outcome':
            if self.outcome_points(instance, points):
                serializer = self.get_serializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "포인트가 부족합니다."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
