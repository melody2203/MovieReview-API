from django.urls import path
from . import views

urlpatterns = [
    # Movie endpoints
    path('', views.MovieList.as_view(), name='movie-list'),
    path('<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),
    
    # Review endpoints
    path('reviews/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    path('<int:movie_id>/reviews/', views.MovieReviewList.as_view(), name='movie-reviews'),
    
    # Authentication endpoints
    path('auth/register/', views.UserCreate.as_view(), name='register'),
    path('auth/login/', views.login, name='login'),

    # User movie lists
    path('user/movies/', views.UserMovieListView.as_view(), name='user-movie-list'),
    path('user/movies/<int:pk>/', views.UserMovieListDetail.as_view(), name='user-movie-detail'),
]