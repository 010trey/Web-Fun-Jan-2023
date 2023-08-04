from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index(): 
    all_users = User.get_all()
    return render_template("index.html", users = all_users)

@app.route('/users/<int:user_id>')
def one_user(user_id):
    # user = User.get_by_id_with_cars({'id':user_id})
    user = User.get_by_id({'id':user_id})
    return render_template("one_user.html", user = user)