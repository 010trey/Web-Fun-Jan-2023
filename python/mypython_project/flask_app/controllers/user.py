from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.product import product
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/registration', methods=['POST'])
def registration():
    # if request.method == 'POST':
    #     user_name = request.form['user_name']
    #     password = request.form['password']
    #     users.append({'user_name': user_name, 'password': password})
    #     return redirect('/login')
    if(User.validate(request.form)):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            **request.form,'password':pw_hash
        }
        user_id = User.create(data)
        session['user_id'] = user_id
        return redirect('/login')
    return redirect('/register')

# action route
@app.route('/process_login', methods=['GET', 'POST'])
def user_login():
    user_from_db = User.get_by_email({'email':request.form['email']})
    if(user_from_db):
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
            flash("Invalid Password","log")
            return redirect('/login')
        session['user_id'] = user_from_db.id
        return redirect('/my_store')
    flash("Invalid Email","log")
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('registration.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


