from rest_framework import serializers
from .models import Reviews
from user_app.models import CustomUser
from restaurants_app.models import Restaurant,Menu

class ReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = '__all__'