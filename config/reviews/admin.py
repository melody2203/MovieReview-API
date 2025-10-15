from django.contrib import admin
from .models import Movie, Review

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'release_date', 'director', 'average_rating']
    list_filter = ['genre', 'release_date']
    search_fields = ['title', 'director']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user_name', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['movie__title', 'user_name']
