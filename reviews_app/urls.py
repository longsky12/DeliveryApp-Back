from django.urls import path

from . import views

# 다른 앱과 URL 별칭이 겹치지 않도록 app name 설정
app_name='reviews'

urlpatterns = [
    path('api/reviews/',views.ReviewsListCreateView.as_view(), name='review-list-create'),
    path('api/reviews/<int:pk>/',views.ReviewsRetrieveUpdateDestroyView.as_view(), name='review-retrieve-update-destroy'),
    path('api/restaurants/<int:restaurant_id>/reviews/',views.RestaurantReviewListAPIView.as_view(), name='restaurant-review-list'),
    
]