# TODO: Feature 6
from app import app
from http import client
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie 
movie_repository = get_movie_repository()

def test_delete_movie():
    # set up test
    app.testing = True
    client = app.test_client()

    #set up movie repo
    movie_repository.clear_db()
    mov1 = movie_repository.create_movie('Hunger Games', "Bay", 9)
    dictall = movie_repository.get_all_movies()
    i =0;
    dict = {}
    for key, value in dictall.items():
        dict[i]=value
        i+=1
    
    # test delete movie
    # response = client.post(f"/movies/{key}/delete")
    movie_repository.delete_movie(key)
    assert movie_repository.get_movie_by_id(key) == None
