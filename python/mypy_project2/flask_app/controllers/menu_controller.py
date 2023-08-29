from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models import  meal_model, category_model, table_model, order_model

# @app.route('/menu/<int:id>')
# def meals_by_category(id):
#     data = {'id': id}
#     category_meals = category_model.Category.get_category_with_meals(data)
#     #print(category)
#     return render_template("category_meals.html", category_meals = category_meals)

@app.route('/menu')
def menu():
    # categories = category_model.Category.get_all_categories()
    meals = meal_model.Meal.get_all_meals()
    data = {'id': session['table_id']}
    # cart_containing = table_model.Table.get_meals_with_table_id(data)
    order_exist = order_model.Order.verify_orders({'table_id': session['table_id']})
    # order_exist = table_model.Table.get_meals_with_table_id(data)
    print("Table meals",order_exist)
    if not order_exist:
        stage0 = {
            'id': session['table_id'],
            'stage': 0
        }
        table_model.Table.update_table_stage(stage0)
    return render_template("menu.html", meals = meals, order_exist = order_exist)

@app.route('/menu/order/add', methods=['post'])
def order():
    data = request.form
    pass
    
@app.route('/session', methods=['post'])
def table_session():
    session['table_id'] = request.form['id']
    # print(session['table_id'])
    data = {
        **request.form,
        'status': 1    
        }
    print('*****', data)
    table_model.Table.update_table_status(data)
    return redirect('/menu')

@app.route('/cart')
def cart_page():
    data = {
        'id': session['table_id']
    }
    # verify session
    table = table_model.Table.get_meals_with_table_id(data)
    return render_template("cart.html", table = table)


