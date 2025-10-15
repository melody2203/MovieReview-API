from rest_framework import generics
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MovieReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Review.objects.filter(movie_id=movie_id)

    def perform_create(self, serializer):
        movie_id = self.kwargs['movie_id']
        movie = Movie.objects.get(id=movie_id)
        serializer.save(movie=movie)
