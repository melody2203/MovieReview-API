import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from movies.models import Movie
from reviews.models import Review

User = get_user_model()

def create_test_data():
    print("Creating test data...")
    
    # Create test user
    user, created = User.objects.get_or_create(
        username='testuser',
        defaults={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
    )
    if created:
        user.set_password('testpass123')
        user.save()
        print(f"✅ Created user: {user.username}")
    else:
        print(f"✅ User already exists: {user.username}")
    
    # Create test movies
    movies_data = [
        {
            'title': 'The Matrix',
            'description': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
            'release_date': '1999-03-31',
            'duration': 136,
            'genre': 'Sci-Fi',
            'director': 'Lana Wachowski, Lilly Wachowski',
            'cast': 'Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss'
        },
        {
            'title': 'Inception',
            'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
            'release_date': '2010-07-16',
            'duration': 148,
            'genre': 'Sci-Fi',
            'director': 'Christopher Nolan',
            'cast': 'Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page'
        },
        {
            'title': 'The Shawshank Redemption',
            'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
            'release_date': '1994-09-23',
            'duration': 142,
            'genre': 'Drama',
            'director': 'Frank Darabont',
            'cast': 'Tim Robbins, Morgan Freeman, Bob Gunton'
        },
        {
            'title': 'The Dark Knight',
            'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
            'release_date': '2008-07-18',
            'duration': 152,
            'genre': 'Action',
            'director': 'Christopher Nolan',
            'cast': 'Christian Bale, Heath Ledger, Aaron Eckhart'
        },
        {
            'title': 'Pulp Fiction',
            'description': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
            'release_date': '1994-10-14',
            'duration': 154,
            'genre': 'Crime',
            'director': 'Quentin Tarantino',
            'cast': 'John Travolta, Uma Thurman, Samuel L. Jackson'
        }
    ]
    
    for movie_data in movies_data:
        movie, created = Movie.objects.get_or_create(
            title=movie_data['title'],
            defaults=movie_data
        )
        if created:
            print(f"✅ Created movie: {movie.title}")
            
            # Create a review for this movie
            review, review_created = Review.objects.get_or_create(
                movie=movie,
                user=user,
                defaults={
                    'rating': 5 if movie.title == 'The Matrix' else 4,
                    'title': f'Great {movie.genre} movie',
                    'content': f'Really enjoyed {movie.title}. The story was engaging and the acting was superb. Highly recommended for {movie.genre} fans!'
                }
            )
            if review_created:
                print(f"✅ Created review for: {movie.title} (Rating: {review.rating} stars)")
            else:
                print(f"✅ Review already exists for: {movie.title}")
        else:
            print(f"✅ Movie already exists: {movie.title}")
    
    print("\n🎉 Test data creation completed!")
    print(f"📊 Summary:")
    print(f"   - Users: {User.objects.count()}")
    print(f"   - Movies: {Movie.objects.count()}")
    print(f"   - Reviews: {Review.objects.count()}")
    print(f"\n🔗 You can now access the API at: http://127.0.0.1:8000/api/")

if __name__ == '__main__':
    create_test_data()
