from flask import Flask, render_template, redirect, request 
from artist_model import Artist
app = Flask(__name__)

# ------------------ALL Artists----------------
# ? GET route 👀
@app.route('/')
def dashboard():
    all_artists = Artist.get_all()
    print("All Artists = ", all_artists, "*"*10)
    # print("🧨"*10,all_artists,"🧨"*10)
    return render_template('dashboard.html', artists = all_artists)

@app.route('/index')
def index():
    all_artists = Artist.get_all()
    return render_template("index.html",artists = all_artists)

# ----------------CREATE NEW ARTIST-----------------
# ? GET route 👀 to see the from
@app.route('/artists/new')
def new_artist():
    return render_template("new_artist.html")

# ? POST route to process the from 📩📩
@app.route('/artists/create', methods=['POST'])
def create_artist():
    # print("*"*20,request.form,"*"*20)
    data_dict = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'nationality':request.form['nationality'],
        'rate':request.form['rate'],
        'image':request.form['image'],
    }
    # data_dict.
    if 'is_dead' in request.form:
        data_dict['is_dead'] = 1
    else:
        data_dict['is_dead'] = 0
    Artist.create_artist(data_dict)
    return redirect('/')
# ------------------------------------------------------

# ---------------------ONE ARTIST-----------------------
@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
    data_dict = {'id':artist_id}
    artist = Artist.get_one_by_id(data_dict)
    return render_template("one_artist.html" , artist = artist)

# ---------------------------UPDATE ARTIST-----------------------

@app.route('/artists/<int:artist_id>/edit')
def edit_artist(artist_id):
    artist_to_update = Artist.get_one_by_id({'id':artist_id})
    return render_template("edit_artist.html", artist = artist_to_update)

@app.route('/artists/<int:artist_id>/update', methods = ['POST'])
def update_artist(artist_id):
    data_dict = {**request.form}
    if 'is_dead' in request.form:
        data_dict['is_dead'] = 1
    else:
        data_dict['is_dead'] = 0
    print("🔥"*10,data_dict, "🔥"*10)
    data_dict['id'] = artist_id
    Artist.update(data_dict)
    return redirect(f'/artists/{artist_id}')


#! Less safe
@app.route('/artists/<int:artist_id>/delete')
def delete(artist_id):
    data_dict = {'id': artist_id}
    Artist.delete(data_dict)
    # redirect always to a route
    return redirect('/')

# ! More safe
@app.route('/artists/<int:artist_id>/destroy', methods=['POST'])
def destroy(artist_id):
    data_dict = {'id': artist_id}
    Artist.delete(data_dict)
    # redirect always to a route
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=5001)