# TODO: Feature 5

from app import app
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

def test_edit_movie():
    test_app = app.test_client()
    movie_repository.clear_db()
    mov1 = movie_repository.create_movie('Hunger Games', "Ross", 5)
    mov2 = movie_repository.create_movie('Drive to Survive', "Formula 1", 3)
    mov3 = movie_repository.create_movie('La La Land', "Ryan", 4)

    #Used this for the .post https://flask.palletsprojects.com/en/2.2.x/testing/
    response = test_app.post(f'/movies/{mov1.movie_id}', data={
        'title': 'The Hunger Games', 
        'director': 'Gary Ross', 
        'rating': 3
    }, follow_redirects=True)
    assert response.status_code == 200

    updatedMov1 = movie_repository.get_movie_by_id(mov1.movie_id)
    assert updatedMov1.title == 'The Hunger Games'
    assert updatedMov1.director == 'Gary Ross'
    assert updatedMov1.rating == 3

    mov2 = movie_repository.get_movie_by_id(mov2.movie_id)
    assert mov2.title == 'Drive to Survive'
    assert mov2.director == 'Formula 1'
    assert mov2.rating == 3

    mov3 = movie_repository.get_movie_by_id(mov3.movie_id)
    assert mov3.title == 'La La Land'
    assert mov3.director == 'Ryan'
    assert mov3.rating == 4