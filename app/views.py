from flask import render_template 
from app import app 


@app.route('/')
def index(): 

    """
        View root page function that returns the index page and its data
    """
    message = "Hello World"
    return render_template('index.html', message=message)


@app.route('/movie/<movie_id>')
def movie(movie_id):

    """
        Route to view details of a single view
    """

    return render_template('movies.html', id=movie_id)



