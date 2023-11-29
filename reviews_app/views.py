from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from rest_framework import generics,status,permissions,authentication
from rest_framework.response import Response

from orders_app.models import Order
from .models import Reviews
from .serializers import ReviewsSerializer
from .permissions import IsOrderFromRestaurant


class ReviewsListCreateView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

    def create(self, request, *args, **kwargs):
        try:
            user = self.request.user

            if user.is_restaurant_admin:
                return Response({"detail": "사장님 계정으로는 리뷰를 작성할 수 없습니다."}, status=status.HTTP_403_FORBIDDEN)

            try:
                order = Order.objects.get(pk=request.data.get('orderId'))
                if order.has_review():
                    return Response({"detail": "이미 리뷰를 작성했습니다."}, status=status.HTTP_403_FORBIDDEN)

                return super().create(request, *args, **kwargs)
            except Order.DoesNotExist:
                return Response({"detail": "주문을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except ValidationError:
            return Response({"detail": "배달이 완료되지 않았거나 주문 하지 않은 가게에는 리뷰를 작성할 수 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        
    def perform_create(self, serializer):
        serializer.save(userId=self.request.user)  # 리뷰를 생성하고 userId를 저장합니다.

class ReviewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsOrderFromRestaurant]

class RestaurantReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return Reviews.objects.filter(restaurantId=restaurant_id)