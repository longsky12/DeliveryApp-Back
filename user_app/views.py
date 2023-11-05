from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("유저 페이지")


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        User.objects.create_user(name=request.data.get('name'),currentAddress=request.data.get('currentAddress'),phone=request.data.get('phone'))
        return Response(serializer.data,status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def user_list(request):
    userList = User.objects.all()
    # serializer = UserSerializer(userList,many=True)
    # return Response(serializer.data,status=201)
    return Response({'data':'123'}, status=201)

# class user_list2(APIView):
#     def get(self,request):
#         userList = User.objects.all()
#         serializer = UserSerializer(userList,many=True)
#         return Response(serializer.data,status=201)