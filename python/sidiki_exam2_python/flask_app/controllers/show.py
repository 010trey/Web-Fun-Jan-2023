from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.show import Show

@app.route('/shows/new')
def new_show():
    if 'user_id' in session:
        return render_template("new_show.html")
    return redirect('/')

@app.route('/shows/create' ,methods=['POST'])
def create_show():
    if(Show.validate(request.form)):
        data = {
            **request.form,'user_id':session['user_id']
        }
        Show.add_show(data)
        return redirect('/dashboard')
    return redirect('/shows/new')

@app.route('/shows/<show_id>/destroy/')
def delete_show(show_id):
    if 'user_id' in session:
        Show.delete({'id':show_id})
    return redirect('/dashboard')

@app.route('/shows/<show_id>/edit')
def edit_show(show_id):
    if 'user_id' in session:
        one_show=Show.get_by_id({'id':show_id})
        return render_template("edit_show.html", show=one_show)
    return redirect('/')

@app.route('/shows/update' ,methods=['POST'])
def update_show():
    if(Show.validate(request.form)):
        Show.edit_show(request.form)
        return redirect('/dashboard')
    return redirect('/shows/'+str(request.form['id'])+'/edit')

@app.route('/shows/<int:show_id>')
def one_show(show_id):
    if 'user_id' in session:
        user = User.get_by_id({'id':session['user_id']})
        one_show=Show.get_by_id({'id':show_id})
        print(one_show)
        return render_template('one_show.html',show=one_show,user=user)
    return redirect('/')