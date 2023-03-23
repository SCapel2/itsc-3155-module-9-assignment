# TODO: Feature 1
from app import app
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

def test_get_all_movies():
    test_app = app.test_client()
    movie_repository.clear_db()
    mov1 = movie_repository.create_movie('Hunger Games', "Bay", 9)
    mov2 = movie_repository.create_movie('Drive to Survive', "Formula 1", 5)
    mov3 = movie_repository.create_movie('La La Land', "Ryan", 7)
    dictall = movie_repository.get_all_movies()
    
    response = test_app.get('/movies')
    assert b'<td>Hunger Games</td>' in response.data #Title
    assert b'<td>Bay</td>' in response.data #Director
    assert b'<td>9</td>' in response.data #Rating

    assert b'<td>Drive to Survive</td>' in response.data #Title
    assert b'<td>Formula 1</td>' in response.data #Director
    assert b'<td>5</td>' in response.data #Rating

    assert b'<td>La La Land</td>' in response.data #Title
    assert b'<td>Ryan</td>' in response.data #Director
    assert b'<td>7</td>' in response.data #Rating