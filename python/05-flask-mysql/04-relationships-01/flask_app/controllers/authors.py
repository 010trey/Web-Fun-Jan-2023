from flask_app import app
from flask import render_template , request, redirect
from flask_app.models.author import Author

@app.route('/')
def index():
    all_authors = Author.get_all()
    return render_template("index.html", authors = all_authors)

@app.route('/authors/create', methods=['POST'])
def create_author():
    Author.create(request.form)
    return redirect('/')

@app.route('/authors/<int:author_id>')
def show_one_author(author_id):
    author = Author.get_one_by_id_with_books({'id': author_id})
    return render_template('one_author.html', author = author)