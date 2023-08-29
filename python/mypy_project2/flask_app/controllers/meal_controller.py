from flask_app import app, ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from flask import render_template, session, redirect, request
import os
from werkzeug.utils import secure_filename

from flask_app.models import category_model
from flask_app.models import meal_model


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/meals')
def meals():
    if 'user_id' not in session:
        return redirect('/signin')
    meals = meal_model.Meal.get_all_meals()
    return render_template("meals.html", meals = meals)

@app.route('/meals/new')
def new_meal():
    if 'user_id' not in session:
        return redirect('/signin')
    categories = category_model.Category.get_all_categories()
    return render_template("add_meal.html", categories = categories)

@app.route('/meals/add', methods=['POST'])
def add_meal():
    print(f'REQUEST FORM {request.form}')
    print(f'REQUEST FILES {request.files}')
    if 'user_id' not in session:
        return redirect('/signin')
    if not meal_model.Meal.validate_meal(request.form):
        return redirect('/meals/new')
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # image with spaces in its name isn't grabed from database
        str_without_spaces = filename.replace(' ', '-')
        file.save(os.path.join(UPLOAD_FOLDER, str_without_spaces))
    data = {
                **request.form,
                'image': str_without_spaces
            }
    meal_model.Meal.add_meal(data)
    return redirect("/meals")

@app.route('/meals/<int:id>/delete')
def delete_meal(id):
    if 'user_id' not in session:
        return redirect('/signin')
    meal_model.Meal.delete_meal({'id':id})
    return redirect('/meals')

@app.route('/meals/<int:id>/edit')
def edit_meal_page(id):
    if 'user_id' not in session:
        redirect('/signin')
    data = {'id': id}
    meal = meal_model.Meal.get_meal_by_id(data)
    categories = category_model.Category.get_all_categories()
    return render_template("edit_meal.html", meal = meal, categories = categories)


@app.route('/meals/edit', methods=['POST'])
def update_meal():
    if not meal_model.Meal.validate_meal(request.form):
        return redirect(f"/meals/{request.form['id']}/edit")
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        str_without_spaces = filename.replace(' ', '-')
        file.save(os.path.join(UPLOAD_FOLDER, str_without_spaces))
    data = { **request.form,
            'image': str_without_spaces
            }
    meal_model.Meal.update_meal(data)
    return redirect("/meals")