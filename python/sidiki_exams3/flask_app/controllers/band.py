from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.band import Band

@app.route('/bands/new')
def new_bands():
    if 'user_id' in session:
        return render_template("new_bands.html")
    return redirect('/')

@app.route('/bands/create' ,methods=['POST'])
def create_bands():
    print(request.form)
    if 'user_id' not in session:
        return redirect('/') 
    if Band.validate(request.form):
        data = {
            **request.form,
            'user_id':session['user_id']
        }
    Band.add_bands(data)
    return redirect('/dashboard')


@app.route('/bands/<bands_id>/destroy/')
def delete_bands(bands_id):
    if 'user_id' in session:
        Band.delete({'id':bands_id})
    return redirect('/dashboard')

@app.route('/bands/<bands_id>/edit')
def edit_bands(bands_id):
    if 'user_id' in session:
        one_bands=Band.get_by_id({'id':bands_id})
        return render_template("edit_bands.html", bands=one_bands)
    return redirect('/')

@app.route('/bands/update' ,methods=['POST'])
def update_band():
    if(Band.validate(request.form)):
        Band.edit_bands(request.form)
        return redirect('/dashboard')
    return redirect('/bands/'+str(request.form['id'])+'/edit')

@app.route('/bands')
def one_bands():
    if 'user_id' in session:
        user = User.get_by_id({'id':session['user_id']})
        mybands=Band.get_by_user({'user_id':session['user_id']})
        print(mybands)
        return render_template('one_bands.html',bands=mybands,user=user)
    return redirect('/')

