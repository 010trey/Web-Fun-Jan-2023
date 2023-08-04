from flask_app import app
from flask import render_template , request, redirect
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books')
def books():
    all_books = Book.get_all()
    all_authors = Author.get_all()
    return render_template("books.html", books = all_books, authors = all_authors)

@app.route('/books/create', methods=['POST'])
def create_book():
    Book.create(request.form)
    return redirect('/books')