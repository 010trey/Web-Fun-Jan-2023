from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' in session:
        return render_template("new_recipe.html")
    return redirect('/')

@app.route('/recipes/create' ,methods=['POST'])
def create_recipe():
    if(Recipe.validate(request.form)):
        data = {
            **request.form,'user_id':session['user_id']
        }
        Recipe.add_recipe(data)
        return redirect('/dashboard')
    return redirect('/recipes/new')

@app.route('/recipes/<recipe_id>/destroy/')
def delete_recipe(recipe_id):
    if 'user_id' in session:
        Recipe.delete({'id':recipe_id})
    return redirect('/dashboard')

@app.route('/recipes/<recipe_id>/edit')
def edit_recipe(recipe_id):
    if 'user_id' in session:
        one_recipe=Recipe.get_by_id({'id':recipe_id})
        return render_template("edit_recipe.html", recipe=one_recipe)
    return redirect('/')

@app.route('/recipes/<recipe_id>/update' ,methods=['POST'])
def update_recipe(recipe_id):
    if(Recipe.validate(request.form)):
        Recipe.edit_recipe(request.form)
        return redirect('/dashboard')
    return redirect('/recipes/'+str(recipe_id)+'/edit')

@app.route('/recipes/<int:recipe_id>')
def one_recipe(recipe_id):
    if 'user_id' in session:
        user = User.get_by_id({'id':session['user_id']})
        one_recipe=Recipe.get_by_id({'id':recipe_id})
        return render_template('one.html',recipe=one_recipe,user=user)
    return redirect('/')
