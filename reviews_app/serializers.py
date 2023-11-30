from rest_framework import serializers
from .models import Reviews, CEOReviews

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class CEOReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CEOReviews
        fields = '__all__'