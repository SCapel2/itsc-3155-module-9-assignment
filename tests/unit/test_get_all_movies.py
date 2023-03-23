# TODO: Feature 1
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()
from src.models.movie import Movie 

def test_get_all_movies():
    movie_repository.clear_db()
    mov1 = movie_repository.create_movie('Hunger Games', "Bay", 9)
    mov2 = movie_repository.create_movie('Drive to Survive', "Formula 1", 5)
    mov3 = movie_repository.create_movie('La La Land', "Ryan", 7)
    dictall = movie_repository.get_all_movies()
    i =0;
    dict = {}
    for key, value in dictall.items():
        dict[i]=value
        i+=1
    
    
    assert len(dict) == 3 #There are 3 movies intialized into the dictionary
    assert dict[0].title == "Hunger Games"
    assert dict[1].title == "Drive to Survive"
    assert dict[2].title == "La La Land"