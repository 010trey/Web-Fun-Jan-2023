from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import category_model

@app.route('/categories')
def categories():
    if 'user_id' not in session:
        return redirect('/signin')
    categories = category_model.Category.get_all_categories()
    return render_template("category.html", categories = categories)

@app.route('/categories/new')
def new_category():
    if 'user_id' not in session:
        return redirect('/signin')
    return render_template("add_category.html")

@app.route('/categories/add', methods=['POST'])
def add_category():
    data = request.form
    category_model.Category.add_category(data)
    return redirect('/categories')