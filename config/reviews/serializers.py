from rest_framework import serializers
from .models import Review
from users.serializers import UserSerializer
from movies.serializers import MovieSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'id', 'movie', 'movie_title', 'user', 'rating', 'title',
            'content', 'created_at', 'updated_at'
        ]
        read_only_fields = ['user']

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['movie', 'rating', 'title', 'content']