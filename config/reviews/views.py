from .models import Movie, Review
from .serializers import UserSerializer, MovieSerializer, ReviewSerializer
from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny

# Import your custom user model safely
try:
    from users.models import CustomUser
    UserModel = CustomUser
except ImportError:
    from django.contrib.auth.models import User
    UserModel = User

class UserCreate(generics.CreateAPIView):
    queryset = UserModel.objects.all()  # ✅ Fixed: Use UserModel, not CustomUser directly
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['POST'])
@authentication_classes([SessionAuthentication])  # Use SessionAuthentication
@permission_classes([AllowAny])  # Allow anyone to access login
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    print(f"🔐 Login attempt - Username: {username}")  # Debug
    
    # Manual authentication for CustomUser
    try:
        from users.models import CustomUser
        user = CustomUser.objects.get(username=username)
        if user.check_password(password):
            print(f"✅ Login successful for user: {user.id}")  # Debug
            return Response({
                'message': 'Login successful', 
                'user_id': user.id,
                'username': user.username
            })
        else:
            print("❌ Invalid password")  # Debug
            return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
    except CustomUser.DoesNotExist:
        print("❌ User not found")  # Debug
        return Response({'error': 'User not found'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        print(f"❌ Error: {e}")  # Debug
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # ✅ Auto-assign logged-in user

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MovieReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # ✅ Added permissions

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Review.objects.filter(movie_id=movie_id)

    def perform_create(self, serializer):
        movie_id = self.kwargs['movie_id']
        movie = Movie.objects.get(id=movie_id)
        serializer.save(movie=movie, user=self.request.user)  # ✅ Auto-assign user