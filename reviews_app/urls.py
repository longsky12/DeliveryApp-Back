from django.urls import path

from . import views

# 다른 앱과 URL 별칭이 겹치지 않도록 app name 설정
app_name='reviews'

urlpatterns = [
    path('api/reviews/',views.ReviewsListCreateView.as_view(), name='review-list-create'),
    path('api/reviews/<int:pk>/',views.ReviewsRetrieveUpdateDestroyView.as_view(), name='review-retrieve-update-destroy'),
    path('api/restaurants/<int:store_id>/reviews/',views.RestaurantReviewListAPIView.as_view(), name='restaurant-review-list'),
    path('api/reviews/<int:review_id>/ceoreviews/',views.CEOReviewsListCreateView.as_view(),name='ceoreview-list-create'),
    path('api/reviews/<int:review_id>/ceoreviews/<int:pk>/',views.CEOReviewsRetrieveUpdateDestroyView.as_view(), name='ceoreview-retrieve-update-destroy'),
]

# GET              api/reviews/         -> 사용자가 작성한 리뷰 가져오기
# POST             api/reviews/         -> 리뷰 생성
# GET              api/reviews/pk/      -> 리뷰 상세 정보 가져오기
# PUT              api/reviews/pk/      -> 리뷰 수정
# DELETE           api/reviews/pk/      -> 리뷰 삭제

# GET               api/restaurants/<int:store_id>/reviews/ -> store_id에 해당하는 식당의 전체 리뷰

# GET               api/reviews/<int:review_id>/ceoreviews/ -> 사장님의 답변
# POST              api/reviews/<int:review_id>/ceoreviews/ -> 사장님의 답변 생성
# GET               api/reviews/<int:review_id>/ceoreviews/pk/ -> 사장님의 답변 상세정보
# PUT               api/reviews/<int:review_id>/ceoreviews/pk/ -> 사장님의 답변 수정
# DELETE            api/reviews/<int:review_id>/ceoreviews/pk/ -> 사장님의 답변 삭제


