from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models import order_model,table_model

@app.route('/order/meal', methods=['POST'])
def add_meal_to_order():
    data = {
            **request.form,
            'table_id': session['table_id']
            }

    # create order with the table_id
    order_model.Order.create_order(data)
    return redirect("/menu")

@app.route('/orders')
def all_orders():
    # orders = table_model.Table.get_orders()
    tables = table_model.Table.get_all_tables()
    orders = []
    for table in tables:
        table_id = {'id': table.id}
        orders.append(table_model.Table.get_meals_with_table_id(table_id))
        print(table_id)
    print ("*** Orders ***", orders)
    return render_template("orders.html", orders = orders)
    
@app.route('/menu/confirm/order', methods=['POST'])
def confirm_order():
    print(request.form)
    data = request.form

    print(str(data))
    table_model.Table.update_table_stage(data)
    return redirect('/menu')

@app.route('/cart/<int:meal_id>/delete')
def delete_meal_from_cart(meal_id):
    data = {
        'meal_id' : meal_id,
        'table_id' : session['table_id']
    }
    order_model.Order.delete_order(data)
    order_exist = order_model.Order.verify_orders({'table_id': session['table_id']})
    if not order_exist:
        stage0 = {
            'id': session['table_id'],
            'stage': 0
        }
        table_model.Table.update_table_stage(stage0)
        return redirect('/menu')
    return redirect('/cart')