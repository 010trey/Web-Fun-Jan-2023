from flask import render_template, request , redirect
from flask_app import app
from flask_app.models.book import Book


@app.route('/books/create', methods=["post"])
def create_book():
    Book.create_book(request.form)
    return redirect('/')