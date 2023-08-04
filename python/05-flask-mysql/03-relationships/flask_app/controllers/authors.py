from flask import render_template, request , redirect
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    all_authors = Author.get_all()
    all_books = Book.get_all()
    return render_template("index.html" ,authors = all_authors, books = all_books)

@app.route('/authors/create', methods=["post"])
def create_author():
    Author.create_author(request.form)
    return redirect('/')