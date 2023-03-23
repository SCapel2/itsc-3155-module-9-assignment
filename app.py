from flask import Flask, request, redirect, render_template

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page

    # Gets form data
    mv_name = request.form.get('movie_name', None, type=str)
    dir_name = request.form.get('director_name', None, type=str)
    rating = request.form.get('rating', None, type=int)

    # Checks if form data is valid
    errors = []

    if mv_name is None or mv_name == '':
        errors.append('Invalid Movie Name')
    if dir_name is None or dir_name == '':
        errors.append('Invalid Director Name')
    if rating is None or rating < 1 or rating > 5:
        errors.append('Invalid Rating')
    
    if errors != []:
        print("!!!!!!")
        return render_template('create_movies_form.html', create_rating_active=True, errors=errors)

    movie_repository.create_movie(mv_name, dir_name, rating)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    return render_template('get_single_movie.html')


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
