from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from rest_framework import generics,status,permissions,authentication
from rest_framework.response import Response

from orders_app.models import Order
from .models import Reviews
from .serializers import ReviewsSerializer


class ReviewsListCreateView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

    def create(self, request, *args, **kwargs):
        try:
            user = self.request.user

            if user.is_restaurant_admin:
                return Response({"message": "사장님 계정으로는 리뷰를 작성할 수 없습니다."}, status=status.HTTP_403_FORBIDDEN)

            try:
                order = Order.objects.get(pk=request.data.get('orderId'))
                if order.has_review():
                    return Response({"message": "이미 리뷰를 작성했습니다."}, status=status.HTTP_403_FORBIDDEN)

                return super().create(request, *args, **kwargs)
            except Order.DoesNotExist:
                return Response({"message": "주문을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except ValidationError:
            return Response({"message": "배달이 완료되지 않았거나 주문 하지 않은 가게에는 리뷰를 작성할 수 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        
    def perform_create(self, serializer):
        serializer.save(userId=self.request.user)  # 리뷰를 생성하고 userId를 저장합니다.

class ReviewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message":"리뷰를 삭제했습니다."},status=status.HTTP_204_NO_CONTENT)

class RestaurantReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewsSerializer
    permission_classes=[permissions.AllowAny]
    def get_queryset(self):
        store_id = self.kwargs['store_id']
        return Reviews.objects.filter(storeId=store_id)