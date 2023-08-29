from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.admin_model import Admin
from flask_app.models.table_model import Table


# ============= display route =============
@app.route('/signin')
def user():
    tables = Table.get_all_tables()
    return render_template('signin.html', tables = tables)

# ============= action routes =============
@app.route('/register', methods=['POST'])
def register():
    if Admin.validate_user(request.form):
        hashed_password = bcrypt.generate_password_hash(request.form['password'])
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_password,
        }
        user_id = Admin.register(data)
        session['user_id']= user_id
        user_from_db = Admin.get_by_email(data)
        session['user_name'] = user_from_db.first_name + " " + user_from_db.last_name
        return redirect('/')
    return redirect('/signin')

@app.route('/login', methods=['POST'])
def login():
    user_from_db = Admin.get_by_email(request.form)
    if not user_from_db:
        flash("Invalid Email / Password", "login_email")
        return redirect('/signin')
    if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        flash("Invalid Email / Password", "login_password")
        return redirect('/signin')
    session['user_name'] = user_from_db.first_name + " " + user_from_db.last_name
    session['user_id']= user_from_db.id
    return redirect('/')

# @app.route('/recipes/new')
# def new_recipe():
#     return render_template("new_recipe.html")

# ============= link route =============
@app.route('/admin/logout')
def logout():
    session.clear()
    return redirect('/')