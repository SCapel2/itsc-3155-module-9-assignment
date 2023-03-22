# TODO: Feature 4
from app import app
from http import client
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie 
movie_repository = get_movie_repository()

def test_get_single_movie():
    # set up test
    app.testing = True
    client = app.test_client()

    #set up movie repo
    movie_repository.clear_db()
    mov1 = movie_repository.create_movie('Mov1', "Dir1", 5)
    dictall = movie_repository.get_all_movies()
    i =0
    dict = {}
    for key, value in dictall.items():
        dict[i]=value
        i+=1

    # test movie is in html page 
    response = client.get(f"/movies/{dict[0].movie_id}")
    assert b'<h1>Mov1</h1>' in response.data
    assert b'<h4>Rating: 5 stars</h4>' in response.data
    assert b'<h2>Director: Dir1</h2>' in response.data