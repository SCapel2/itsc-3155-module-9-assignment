# TODO: Feature 2
from app import app
from http import client
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repository = get_movie_repository()

# Case 1: Valid movie name, director name and rating
def test_create_valid_movies():
    app.testing = True
    client = app.test_client()
    
    response = client.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': 3})
    assert response.status_code == 302 
    all_movies = movie_repository.get_all_movies()
    assert len(all_movies) == 1
    for movie in all_movies.values():
        assert movie.title == 'Hunger Games'
        assert movie.director == 'Gary Ross'
        assert movie.rating == 3

    movie_repository.clear_db()

# Case 2: No movie name
def test_create_invalid_name_1():
    app.testing = True
    client = app.test_client()

    response = client.post('/movies', data={'movie_name': None, 'director_name': 'Gary Ross', 'rating': 3})
    all_movies = movie_repository.get_all_movies()

    assert len(all_movies) == 0
    movie_repository.clear_db()

# Case 3: No director name
def test_create_invalid_director_1():
    app.testing = True
    client = app.test_client()

    response = client.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': None, 'rating': 3})
    all_movies = movie_repository.get_all_movies()
    assert len(all_movies) == 0
    movie_repository.clear_db()

# Case 4a: No rating
def test_create_invalid_rating_1():
    app.testing = True
    client = app.test_client()

    response = client.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': None})
    all_movies = movie_repository.get_all_movies()
    assert len(all_movies) == 0
    movie_repository.clear_db()

# Case 4b: Non-integer rating
def test_create_invalid_rating_2():
    app.testing = True
    client = app.test_client()

    response = client.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': 'abc'})
    all_movies = movie_repository.get_all_movies()
    assert len(all_movies) == 0
    movie_repository.clear_db()

# Case 4c: Rating out of range (>5)
def test_create_invalid_rating_3():
    app.testing = True
    client = app.test_client()

    response = client.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': 6})
    all_movies = movie_repository.get_all_movies()
    assert len(all_movies) == 0
    movie_repository.clear_db()

# Case 4d: Rating out of range (<0)
def test_create_invalid_rating_4():
    app.testing = True
    client = app.test_client()
    
    response = client.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': 0})
    all_movies = movie_repository.get_all_movies()
    assert len(all_movies) == 0
    movie_repository.clear_db()