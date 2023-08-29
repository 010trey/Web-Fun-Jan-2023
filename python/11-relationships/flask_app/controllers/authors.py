
# FUNCTIONS AND UTILS FROM flask 
from flask import render_template, request, redirect, url_for
# app TO CREATE ROUTES
from flask_app import app
# Author models(class) to execute methods
from flask_app.models.author import Author


@app.route('/')
def index():
    authors = Author.get_all()
    # Author.get_by_id_with_quotes({'id':2})
    return render_template('index.html', authors = authors)

@app.route('/authors/create', methods=['POST'])
def create():
    Author.create(request.form)
    return redirect('/')

@app.route('/authors/<int:author_id>')
def one_author(author_id):
    # author = Author.get_by_id_with_quotes({'id':author_id})
    author = Author.get_by_id({'id':author_id})
    return render_template("one_author.html", author=author)

"""
[
    {
        'id': 3, 'name': 'Elon Mask', 'country': 'USA', 
        'created_at': datetime.datetime(2023, 8, 3, 9, 31, 56), 
        'updated_at': datetime.datetime(2023, 8, 3, 9, 31, 56)
        }
    ]
"""