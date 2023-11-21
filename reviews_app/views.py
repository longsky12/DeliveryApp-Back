from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import Reviews
from .serializers import ReviewsSerializer
from .permissions import IsOrderFromRestaurant

class ReviewsListCreateView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsOrderFromRestaurant]

class ReviewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsOrderFromRestaurant]

class RestaurantReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return Reviews.objects.filter(restaurantId=restaurant_id)