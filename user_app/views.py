from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("유저 페이지")

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {'message':'Hello, Rest API!'}
    return Response(data)