# TODO: Feature 2
from app import app
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

# Case 1: app.get('/movies/new') should return a 200 status code
def test_create_movie_page_format():
    test_app = app.test_client()
    response = test_app.get('/movies/new')

    assert response.status_code == 200

# Case 2: app.get('/movies/new') should return the correct HTML
    test_app = app.test_client()
    response = test_app.get('/movies/new')

    assert b'<p class="mb-3">Create a movie rating below</p>' in response.data
    assert b'<label for="movie_name">Movie Name</label>' in response.data
    assert b'<label for="director_name">Director Name</label>' in response.data
    assert b'<label for="rating">Rating</label>' in response.data

# Case 3: Valid movie name, director name and rating should return 302 status code
def test_create_valid_movies():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()
    
    response = client.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': 3})
    assert response.status_code == 302 
    all_movies = movie_repository.get_all_movies()
    assert len(all_movies) == 1
    for movie in all_movies.values():
        assert movie.title == 'Hunger Games'
        assert movie.director == 'Gary Ross'
        assert movie.rating == 3

    movie_repository.clear_db()

# Case 4: No movie name should not create a movie
def test_create_invalid_name_1():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()

    response = client.post('/movies', data={'movie_name': None, 'director_name': 'Gary Ross', 'rating': 3})
    all_movies = movie_repository.get_all_movies()

    assert len(all_movies) == 0
    movie_repository.clear_db()

# Case 5: No director name should not create a movie
def test_create_invalid_director_1():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()

    response = client.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': None, 'rating': 3})
    all_movies = movie_repository.get_all_movies()
    assert len(all_movies) == 0
    movie_repository.clear_db()

# Case 6a: No rating should not create a movie
def test_create_invalid_rating_1():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()

    response = client.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': None})
    all_movies = movie_repository.get_all_movies()
    assert len(all_movies) == 0
    movie_repository.clear_db()

# Case 6b: Non-integer rating should not create a movie
def test_create_invalid_rating_2():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()

    response = client.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': 'abc'})
    all_movies = movie_repository.get_all_movies()
    assert len(all_movies) == 0
    movie_repository.clear_db()

# Case 6c: Rating out of range (>5) should not create a movie
def test_create_invalid_rating_3():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()

    response = client.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': 6})
    all_movies = movie_repository.get_all_movies()
    assert len(all_movies) == 0
    movie_repository.clear_db()

# Case 6d: Rating out of range (<0) should not create a movie
def test_create_invalid_rating_4():
    app.testing = True
    client = app.test_client()
    movie_repository.clear_db()
    
    response = client.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': 0})
    all_movies = movie_repository.get_all_movies()
    assert len(all_movies) == 0
    movie_repository.clear_db()