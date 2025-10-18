from django.conf import settings
from rest_framework import serializers
from .models import Movie, Review

# Import your custom user model safely
try:
    from users.models import CustomUser
    UserModel = CustomUser
except ImportError:
    from django.contrib.auth.models import User
    UserModel = User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # ✅ Fixed: UserSerializer, not serializers
    # Remove user_id field since we'll auto-assign the logged-in user
    
    class Meta:
        model = Review
        fields = ['id', 'movie', 'user', 'rating', 'content', 'created_at', 'updated_at']  # ✅ Remove user_name
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']

class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.ReadOnlyField()
    total_reviews = serializers.ReadOnlyField()
    
    class Meta:
        model = Movie
        fields = '__all__'