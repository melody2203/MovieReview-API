from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Sci-Fi', 'Science Fiction'),
        ('Romance', 'Romance'),
        ('Thriller', 'Thriller'),
        ('Fantasy', 'Fantasy'),
        ('Animation', 'Animation'),
        ('Documentary', 'Documentary'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    director = models.CharField(max_length=100)
    cast = models.TextField(help_text="Main cast members")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-release_date']

    def __str__(self):
        return self.title
    
    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return round(sum(review.rating for review in reviews) / len(reviews), 1)
        return 0
    
    @property
    def total_reviews(self):
        return self.reviews.count()
