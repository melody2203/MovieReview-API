from django.urls import path
from . import views

urlpatterns = [
    # Movie URLs
    path('movies/', views.MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),
    
    # Review URLs
    path('reviews/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    path('movies/<int:movie_id>/reviews/', views.MovieReviewList.as_view(), name='movie-reviews'),
]