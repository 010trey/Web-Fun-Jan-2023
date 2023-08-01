from flask import Flask , render_template, request, redirect, session

app  = Flask(__name__)
app.secret_key = "No Secrets in GitHub"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("*"*20, "PROCESS - FORM RECEIVED ","*"*20)
    print("-"*20, request.form,"-"*20)
    print(f"USERNAME : {request.form['username']}\nAGE : {request.form['age']}\nFAVORITE FOOD: {request.form['fav_food']}")
    # ! NEVER EVER RENDER ON POST REQUEST
    # return render_template('display.html', username = request.form['username'],  age = request.form['age'],  fav_food = request.form['fav_food'])
    session['username'] = request.form['username']
    session['age'] = request.form['age']
    session['fav_food'] = request.form['fav_food']
    # ? BROWSER SESSION : .eJyrVkpMT1WyUjI2VdJRSkssi0_Lz08B8mNKUyyMU4BkqkEqMhuoqrQ4tSgvMRekKzgxV6kWAMHIFVc.ZLUjuQ.FxwfmfltyI2GM6Tz16lBU5uvCpE
    return redirect('/display')

@app.route('/display')
def display():
    print("🎈"*20,request.form,"🎈"*20)
    # print(session['username'] )
    # print(session['age'] )
    # print(session['fav_food'] )
    return render_template("display.html")

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/display')

if __name__ =='__main__':
    app.run(debug = True, port=5003)