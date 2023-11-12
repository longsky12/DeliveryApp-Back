from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, OrderMenu
from .serializers import OrderSerializer, OrderMenuSerializer

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("주문 페이지")

# CreateAPIView only create : POST
# ListCreateAPIView create & list : POST & GET
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# RetrieveUpdateDestroyAPIView : POST, PATCH, DELETE
class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

