from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html",user = logged_user)

@app.route('/users/create', methods=['POST'])
def register():
    print("🔥"*20,request.form,"🔥"*20)
    if User.validate_register(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print("Password : ", request.form['password'])
        print("Hashed Password : ", pw_hash)
        data_dict = {
            **request.form,
            'password':pw_hash
        }
        # print(request.form,"--------------------")
        # print(data_dict,"**************************")
        # b'$2b$12$PQzrVLpEuqq8YZOA0RAKo.u3X9.1pDGtannCoANYulfQpbhvCano6 == 1111111
        user_id = User.create(data_dict)
        session['user_id'] = user_id
        return redirect('/dashboard')
    return redirect('/')

@app.route('/login', methods =['POST'])
def login():
    print(request.form)
    user_from_db = User.get_by_email({'email':request.form['email']})
    print(user_from_db)
    if user_from_db:
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
            # if we get False after checking the password
            flash("Wrong Password !!!","login")
            return redirect('/')
        session['user_id'] = user_from_db.id
        return redirect('/dashboard')
    flash("Wrong email !!!!","login")
    return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')