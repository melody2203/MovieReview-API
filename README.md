# MovieReview API

A RESTful API for movie reviews and ratings built with Django REST Framework.

## Features

- User authentication with JWT
- Movie management
- Review system with ratings (1-5 stars)
- Average rating calculations
- Search and filtering

## Tech Stack

- Django 4.2
- Django REST Framework
- JWT Authentication
- SQLite (Development)

## Quick Start

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`

## API Endpoints

- `POST /api/users/register/` - User registration
- `POST /api/token/` - Get JWT token
- `GET /api/movies/` - List all movies
- `GET /api/reviews/` - List all reviews
- `POST /api/reviews/` - Create a review

## Project Structure

```
