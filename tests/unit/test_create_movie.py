# TODO: Feature 2
from app import app
from http import client
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repository = get_movie_repository()

# Case 1: Valid movie name, director name and rating should create a movie
def test_create_valid_movies():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()
    
    test_movie = movie_repository.create_movie('Hunger Games', 'Gary Ross', 3)
    assert test_movie.title == 'Hunger Games'
    assert test_movie.director == 'Gary Ross'
    assert test_movie.rating == 3
    assert len(movie_repository.get_all_movies()) == 1

    movie_repository.clear_db()

# Case 2: No movie name should create a movie
def test_create_invalid_name_1():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()

    test_movie = movie_repository.create_movie(None, 'Gary Ross', 3)
    assert test_movie.title == None
    assert test_movie.director == 'Gary Ross'
    assert test_movie.rating == 3

    assert len(movie_repository.get_all_movies()) == 1

    movie_repository.clear_db()

# Case 3: No director name should create a movie
def test_create_invalid_director_1():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()

    test_movie = movie_repository.create_movie('Hunger Games', None, 3)
    assert test_movie.title == 'Hunger Games'
    assert test_movie.director == None
    assert test_movie.rating == 3
    assert len(movie_repository.get_all_movies()) == 1

    movie_repository.clear_db()

# Case 4a: No rating should create a movie
def test_create_invalid_rating_1():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()

    test_movie = movie_repository.create_movie('Hunger Games', 'Gary Ross', None)
    assert test_movie.title == 'Hunger Games'
    assert test_movie.director == 'Gary Ross'
    assert test_movie.rating == None
    assert len(movie_repository.get_all_movies()) == 1

    movie_repository.clear_db()

# Case 4b: Non-integer rating should create a movie
def test_create_invalid_rating_2():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()

    test_movie = movie_repository.create_movie('Hunger Games', 'Gary Ross', 'abc')
    assert test_movie.title == 'Hunger Games'
    assert test_movie.director == 'Gary Ross'
    assert test_movie.rating == 'abc'
    assert len(movie_repository.get_all_movies()) == 1

    movie_repository.clear_db()

# Case 4c: Rating out of range (>5) should create a movie
def test_create_invalid_rating_3():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()

    test_movie = movie_repository.create_movie('Hunger Games', 'Gary Ross', 6)
    assert test_movie.title == 'Hunger Games'
    assert test_movie.director == 'Gary Ross'
    assert test_movie.rating == 6
    assert len(movie_repository.get_all_movies()) == 1

    movie_repository.clear_db()

# Case 4d: Rating out of range (<1)
def test_create_invalid_rating_4():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()

    test_movie = movie_repository.create_movie('Hunger Games', 'Gary Ross', 0)
    assert test_movie.title == 'Hunger Games'
    assert test_movie.director == 'Gary Ross'
    assert test_movie.rating == 0
    assert len(movie_repository.get_all_movies()) == 1
    
    movie_repository.clear_db()