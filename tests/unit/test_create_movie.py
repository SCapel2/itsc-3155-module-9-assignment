# TODO: Feature 2
from app import app

# Case 1: Valid movie name, director name and rating
def test_valid_creation():
    assert app.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': 3}).status_code == 302

# Case 2: Invalid movie name
def test_invalid_movie_name():
    # 2a: No movie name
    assert app.post('/movies', data={'movie_name': None, 'director_name': 'Gary Ross', 'rating': 3}).status_code == 480
    assert app.post('/movies', data={'movie_name': None, 'director_name': 'Gary Ross', 'rating': 3}).errors == ['Invalid Movie Name']

    # 2b: Non-string movie name
    assert app.post('/movies', data={'movie_name': 123, 'director_name': 'Gary Ross', 'rating': 3}).status_code == 480
    assert app.post('/movies', data={'movie_name': 123, 'director_name': 'Gary Ross', 'rating': 3}).errors == ['Invalid Movie Name']

# Case 3: Invalid director name
def test_invalid_director_name():
    # 3a: No director name
    assert app.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': None, 'rating': 3}).status_code == 480
    assert app.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': None, 'rating': 3}).errors == ['Invalid Director Name']

    # 3b: Non-string director name
    assert app.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 123, 'rating': 3}).status_code == 480
    assert app.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 123, 'rating': 3}).errors == ['Invalid Director Name']

# Case 4: Invalid rating
def test_invalid_rating():
    # 4a: No rating
    assert app.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': None}).status_code == 480
    assert app.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': None}).errors == ['Invalid Rating']

    # 4b: Non-integer rating
    assert app.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': 'abc'}).status_code == 480
    assert app.post('/movies', data={'movie_name': 'Hunger Games', 'director_name': 'Gary Ross', 'rating': 'abc'}).errors == ['Invalid Rating']

# Case 5: All invalid fields
def test_invalid_all_fields():
    # 5a: No movie name, no director name, no rating
    assert app.post('/movies', data={'movie_name': None, 'director_name': None, 'rating': None}).status_code == 480
    assert app.post('/movies', data={'movie_name': None, 'director_name': None, 'rating': None}).errors == ['Invalid Movie Name', 'Invalid Director Name', 'Invalid Rating']

    # 5b: No movie name, no director name, non-integer rating
    assert app.post('/movies', data={'movie_name': None, 'director_name': None, 'rating': 'abc'}).status_code == 480
    assert app.post('/movies', data={'movie_name': None, 'director_name': None, 'rating': 'abc'}).errors == ['Invalid Movie Name', 'Invalid Director Name', 'Invalid Rating']

    # 5c: No movie name, non-string director name, no rating
    assert app.post('/movies', data={'movie_name': None, 'director_name': 123, 'rating': None}).status_code == 480
    assert app.post('/movies', data={'movie_name': None, 'director_name': 123, 'rating': None}).errors == ['Invalid Movie Name', 'Invalid Director Name', 'Invalid Rating']

    # 5d: No movie name, non-string director name, non-integer rating
    assert app.post('/movies', data={'movie_name': None, 'director_name': 123, 'rating': 'abc'}).status_code == 480
    assert app.post('/movies', data={'movie_name': None, 'director_name': 123, 'rating': 'abc'}).errors == ['Invalid Movie Name', 'Invalid Director Name', 'Invalid Rating']

    # 5e: Non-string movie name, no director name, no rating
    assert app.post('/movies', data={'movie_name': 123, 'director_name': None, 'rating': None}).status_code == 480
    assert app.post('/movies', data={'movie_name': 123, 'director_name': None, 'rating': None}).errors == ['Invalid Movie Name', 'Invalid Director Name', 'Invalid Rating']

    # 5f: Non-string movie name, no director name, non-integer rating
    assert app.post('/movies', data={'movie_name': 123, 'director_name': None, 'rating': 'abc'}).status_code == 480
    assert app.post('/movies', data={'movie_name': 123, 'director_name': None, 'rating': 'abc'}).errors == ['Invalid Movie Name', 'Invalid Director Name', 'Invalid Rating']

    # 5g: Non-string movie name, non-string director name, no rating
    assert app.post('/movies', data={'movie_name': 123, 'director_name': 123, 'rating': None}).status_code == 480
    assert app.post('/movies', data={'movie_name': 123, 'director_name': 123, 'rating': None}).errors == ['Invalid Movie Name', 'Invalid Director Name', 'Invalid Rating']

    # 5h: Non-string movie name, non-string director name, non-integer rating
    assert app.post('/movies', data={'movie_name': 123, 'director_name': 123, 'rating': 'abc'}).status_code == 480
    assert app.post('/movies', data={'movie_name': 123, 'director_name': 123, 'rating': 'abc'}).errors == ['Invalid Movie Name', 'Invalid Director Name', 'Invalid Rating']

# Case 6: 2 invalid fields movie name
def test_invalid_movie_name_and_director_name():
    # 6a: No movie name, no director name
    assert app.post('/movies', data={'movie_name': None, 'director_name': None, 'rating': 3}).status_code == 480
    assert app.post('/movies', data={'movie_name': None, 'director_name': None, 'rating': 3}).errors == ['Invalid Movie Name', 'Invalid Director Name']

    # 6b: No movie name, non-string director name
    assert app.post('/movies', data={'movie_name': None, 'director_name': 123, 'rating': 3}).status_code == 480
    assert app.post('/movies', data={'movie_name': None, 'director_name': 123, 'rating': 3}).errors == ['Invalid Movie Name', 'Invalid Director Name']

    # 6c: Non-string movie name, no director name
    assert app.post('/movies', data={'movie_name': 123, 'director_name': None, 'rating': 3}).status_code == 480
    assert app.post('/movies', data={'movie_name': 123, 'director_name': None, 'rating': 3}).errors == ['Invalid Movie Name', 'Invalid Director Name']

    # 6d: Non-string movie name, non-string director name
    assert app.post('/movies', data={'movie_name': 123, 'director_name': 123, 'rating': 3}).status_code == 480
    assert app.post('/movies', data={'movie_name': 123, 'director_name': 123, 'rating': 3}).errors == ['Invalid Movie Name', 'Invalid Director Name']

def test_invalid_movie_name_and_rating():
    # 7a: No movie name, no rating
    assert app.post('/movies', data={'movie_name': None, 'director_name': 'Gary Ross', 'rating': None}).status_code == 480
    assert app.post('/movies', data={'movie_name': None, 'director_name': 'Gary Ross', 'rating': None}).errors == ['Invalid Movie Name', 'Invalid Rating']

    # 7b: No movie name, non-integer rating
    assert app.post('/movies', data={'movie_name': None, 'director_name': 'Gary Ross', 'rating': 'abc'}).status_code == 480
    assert app.post('/movies', data={'movie_name': None, 'director_name': 'Gary Ross', 'rating': 'abc'}).errors == ['Invalid Movie Name', 'Invalid Rating']

    # 7c: Non-string movie name, no rating
    assert app.post('/movies', data={'movie_name': 123, 'director_name': 'Gary Ross', 'rating': None}).status_code == 480
    assert app.post('/movies', data={'movie_name': 123, 'director_name': 'Gary Ross', 'rating': None}).errors == ['Invalid Movie Name', 'Invalid Rating']

    # 7d: Non-string movie name, non-integer rating
    assert app.post('/movies', data={'movie_name': 123, 'director_name': 'Gary Ross', 'rating': 'abc'}).status_code == 480
    assert app.post('/movies', data={'movie_name': 123, 'director_name': 'Gary Ross', 'rating': 'abc'}).errors == ['Invalid Movie Name', 'Invalid Rating']

def test_invalid_director_name_and_rating():
    # 8a: No director name, no rating
    assert app.post('/movies', data={'movie_name': 'The Hunger Games', 'director_name': None, 'rating': None}).status_code == 480
    assert app.post('/movies', data={'movie_name': 'The Hunger Games', 'director_name': None, 'rating': None}).errors == ['Invalid Director Name', 'Invalid Rating']

    # 8b: No director name, non-integer rating
    assert app.post('/movies', data={'movie_name': 'The Hunger Games', 'director_name': None, 'rating': 'abc'}).status_code == 480
    assert app.post('/movies', data={'movie_name': 'The Hunger Games', 'director_name': None, 'rating': 'abc'}).errors == ['Invalid Director Name', 'Invalid Rating']

    # 8c: Non-string director name, no rating
    assert app.post('/movies', data={'movie_name': 'The Hunger Games', 'director_name': 123, 'rating': None}).status_code == 480
    assert app.post('/movies', data={'movie_name': 'The Hunger Games', 'director_name': 123, 'rating': None}).errors == ['Invalid Director Name', 'Invalid Rating']

    # 8d: Non-string director name, non-integer rating
    assert app.post('/movies', data={'movie_name': 'The Hunger Games', 'director_name': 123, 'rating': 'abc'}).status_code == 480
    assert app.post('/movies', data={'movie_name': 'The Hunger Games', 'director_name': 123, 'rating': 'abc'}).errors == ['Invalid Director Name', 'Invalid Rating']
