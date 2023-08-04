from flask import Flask, render_template, request, redirect, session

app  = Flask(__name__)
app.secret_key = "No secrets"
# http://127.0.0.1:5003
# http://localhost:5003
@app.route('/', methods=['GET']) #GET Route TO SEE THE FROM 👀
def index():
    # print(r)
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    print("Request From Dash :", request.form)
    username = session['username']
    return render_template('dashboard.html', username = username)

@app.route('/process', methods=['POST'])
def process():
    print("FORM DATA : ",request.form, "*"*20)
    # session
    session['username'] = request.form['username']
    session['age'] = request.form['age']
    session['fav_food'] = request.form['fav_food']
    session['fav_sport'] = request.form['fav_sport']
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True, port=5003)