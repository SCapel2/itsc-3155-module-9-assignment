# TODO: Feature 4
#from app import app
from http import client
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie 
movie_repository = get_movie_repository()

def test_get_single_movie():
    # set up test
    #app.testing = True
    #client = app.test_client()

    #set up movie repo
    movie_repository.clear_db()
    mov1 = movie_repository.create_movie( 'Mov1', 'Dir1', 5)
    dictall = movie_repository.get_all_movies()
    i = 0
    dict = {}
    for key, value in dictall.items():
        dict[i] = value
        i+=1

    # test movie is in html page 
    response = movie_repository.get_movie_by_id(dict[0].movie_id)
    assert response.title == 'Mov1'
    assert response.director == 'Dir1'
    assert response.rating == 5
