from flask import Flask

app = Flask(__name__)
app.secret_key= "Stay Safe"
DATABASE = "exams_db"