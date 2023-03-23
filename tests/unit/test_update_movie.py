# TODO: Feature 5

from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()
from src.models.movie import Movie 

def test_edit_movie():
    movie_repository.clear_db()
    mov1 = movie_repository.create_movie('Hunger Games', "Bay", 5)
    mov2 = movie_repository.create_movie('Drive to Survive', "Formula 1", 3)
    mov3 = movie_repository.create_movie('La La Land', "Ryan", 4)
    Updatedmov1 = movie_repository.update_movie(mov1.movie_id, "The Hunger Games", "Michael Bay", 3)

    dictall = movie_repository.get_all_movies()
    i =0;
    dict = {}
    for key, value in dictall.items():
        dict[i]=value
        i+=1


    assert len(dict) == 3
    assert dict[0].title == "The Hunger Games"
    assert dict[0].director == "Michael Bay"
    assert dict[0].rating == 3