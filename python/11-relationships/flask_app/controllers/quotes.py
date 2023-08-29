# FUNCTIONS AND UTILS FROM flask 
from flask import render_template, request, redirect
# app TO CREATE ROUTES
from flask_app import app
# Author models(class) to execute methods
from flask_app.models.quote import Quote
from flask_app.models.author import Author

@app.route('/quotes')
def quotes():
    quotes = Quote.get_all()
    return render_template('all_quotes.html', quotes=quotes)

@app.route('/quotes/new')
def new_quotes():
    authors = Author.get_all()
    return render_template('new_quote.html', authors=authors)

@app.route('/quotes/create', methods=['POST'])
def create_quote():
    print("*"*10,request.form,"*"*10)
    Quote.create(request.form)
    return redirect('/quotes')