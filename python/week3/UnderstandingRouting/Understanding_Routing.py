from flask import Flask  
app = Flask(__name__)  


# Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'DOJO'

@app.route('/say/<name>')
def test(name):
    return 'hi '+name

@app.route('/repeat/<int:num>/<text>')
def repeat(num,text):
    output=""
    for i in range(num) :
        output+=text
    
    return output




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
    

