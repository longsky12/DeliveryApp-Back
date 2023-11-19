# TEST 용도
from django.http import JsonResponse
from django.views import View



from .models import CustomUser
from rest_framework import generics, status
from rest_framework.response import Response
from.serializers import RegisterSerializer, LoginSerializer

# POST
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        serializer.save(is_restaurant_admin=self.request.data.get('is_restaurant_admin',False))

# POST
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        token = serializer.validated_data
        return Response({"token":token.key}, status = status.HTTP_200_OK)

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views

# GET
class CustomLogoutView(auth_views.LogoutView):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
# Test 용도
class CustomUserListView(View):
    def get(self,request,*args,**kwargs):
        users = CustomUser.objects.all()
        user_list = list(users.values())
        return JsonResponse({'users':user_list})