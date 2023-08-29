from flask_app import app
from flask import render_template, session, redirect, request

from flask_app.models import table_model
from flask_app.models.meal_model import Meal

@app.route('/')
def dashboard():
    if 'user_id' not in session:
        return redirect('/signin')
    tables = table_model.Table.get_all_tables()
    return render_template("index.html", tables = tables)

@app.route('/tables')
def tables():
    if 'user_id' not in session:
        return redirect('/signin')
    tables = table_model.Table.get_all_tables()
    return render_template("tables.html", tables = tables)

@app.route('/tables/new')
def new_table_page():
    if 'user_id' not in session:
        return redirect('/signin')
    return render_template("add_table.html")

@app.route('/tables/add', methods=['post'])
def add_table():
    data = request.form
    table_model.Table.add_table(data)
    return redirect('/tables')

@app.route('/tables/order/<int:table_id>')
def table_order(table_id):
    if 'user_id' not in session:
        return redirect('/signin')
    # ordered_meals = meal_model.Meal.get_ordered_meals({'table_id':table_id})
    # for meal in ordered_meals:
    #     print(meal.name,"\n")
    table_order = table_model.Table.get_meals_with_table_id({'id':table_id})

    return render_template("table_meals.html", table_order = table_order)

@app.route('/tables/change/stage', methods=['POST'])
def change_table_stage():
    print(request.form)
    data = request.form

    print(str(data))
    table_model.Table.update_table_stage(data)
    return redirect('/')