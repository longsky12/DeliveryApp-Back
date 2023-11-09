from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("레스토랑 페이지")

# Restaurant CRUD
class RestaurantCreateView(APIView):
    def post(self,request,format=None):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantRetrieveView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantUpdateView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDestroyView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# Menu CRUD
class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuListByStoreIdView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        store_id = self.kwargs['storeId']
        queryset = Menu.objects.filter(storeId=store_id)
        return queryset
    
class MenuRetrieveView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuUpdateView(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDestroyView(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
# MenuOption CRUD