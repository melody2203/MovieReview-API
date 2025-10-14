from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.ReadOnlyField()
    total_reviews = serializers.ReadOnlyField()
    
    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'description', 'release_date', 'duration',
            'genre', 'director', 'cast', 'poster', 'average_rating',
            'total_reviews', 'created_at', 'updated_at'
        ]