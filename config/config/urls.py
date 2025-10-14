from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication - Using DRF's built-in token auth
    path('api/auth-token/', obtain_auth_token, name='api_token_auth'),
    
    # API endpoints
    path('api/users/', include('users.urls')),
    path('api/movies/', include('movies.urls')),
    path('api/reviews/', include('reviews.urls')),
]