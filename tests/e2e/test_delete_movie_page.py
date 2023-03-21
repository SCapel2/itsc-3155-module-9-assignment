# TODO: Feature 6
from app import app
from http import client
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie 
movie_repository = get_movie_repository()

def test_delete_movie_page():
    # set up
    test_app = app.test_client()

    # set up movie repo
    movie_repository.clear_db()
    mov1 = movie_repository.create_movie('Hunger Games', "Bay", 9)
    mov2 = movie_repository.create_movie('Drive to Survive', "Formula 1", 5)
    mov3 = movie_repository.create_movie('La La Land', "Ryan", 7)
    dictall = movie_repository.get_all_movies()
    
    # delete first movie
    response = test_app.post(f"/movies/1/delete")
    assert b'<td>Hunger Games</td>' not in response.data #Title
    assert b'<td>Bay</td>' not in response.data #Director
    assert b'<td>9</td>' not in response.data #Rating
    assert movie_repository.get_movie_by_id(1) == None

    # delete second movie
    response = test_app.post(f"/movies/2/delete")
    assert b'<td>Drive to Survive</td>' not in response.data #Title
    assert b'<td>Formula 1</td>' not in response.data #Director
    assert b'<td>5</td>' not in response.data #Rating
    assert movie_repository.get_movie_by_id(2) == None

    # delete third movie
    response = test_app.post(f"/movies/3/delete")
    assert b'<td>La La Land</td>' not in response.data #Title
    assert b'<td>Ryan</td>' not in response.data #Director
    assert b'<td>7</td>' not in response.data #Rating
    assert movie_repository.get_movie_by_id(3) == None