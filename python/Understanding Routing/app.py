from flask import Flask

app = Flask(__name__)

# Route for localhost:5000/
@app.route('/')
def hello_world():
    return "Hello World!"

# Route for localhost:5000/dojo
@app.route('/dojo')
def dojo():
    return "Dojo!"

# Route for localhost:5000/say/<name>
@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"

# Route for localhost:5000/repeat/<int:num>/<word>
@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    return word * num

if __name__ == '__main__':
    app.run(debug=True)
