# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie


movie_repository = get_movie_repository()


def test_get_movie_by_title():
    movie1 = movie_repository.get_movie_by_title("Hunger Games")
    movie2 = movie_repository.get_movie_by_title('Drive to Survive')
    movie3 = movie_repository.get_movie_by_title('La La Land')


    rating1 = movie1.rating
    rating2 = movie2.rating
    rating3 = movie3.rating


    assert rating1 == 9
    assert rating2== 5
    assert rating3 == 7