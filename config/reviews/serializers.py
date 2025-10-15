from rest_framework import serializers
from .models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'user_name', 'rating', 'comment', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.ReadOnlyField()
    total_reviews = serializers.ReadOnlyField()
    
    class Meta:
        model = Movie
        fields = '__all__'