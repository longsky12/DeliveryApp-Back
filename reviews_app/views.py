from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,status,permissions
from rest_framework.response import Response

from .models import Reviews
from .serializers import ReviewsSerializer
from .permissions import IsOrderFromRestaurant

class ReviewsListCreateView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self,request, *args, **kwargs):
        restaurant_id = request.data.get('storeId')
        # 주문 여부 확인 로직 필요
        

        # 주문 했다고 가정
        order_from_restaurant = True
        
        if order_from_restaurant:
            return super().create(request,*args,**kwargs)
        else:
            return Response({"message":"You must have ordered from this restaurant to leave a review."},status=status.HTTP_403_FORBIDDEN)

    def perform_create(self, serializer):
        serializer.save(userId=self.request.user)


class ReviewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsOrderFromRestaurant]

class RestaurantReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return Reviews.objects.filter(restaurantId=restaurant_id)