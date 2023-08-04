from flask import Flask

app = Flask(__name__)
app.secret_key = "vdfknbvlkfnbkd"
DATABASE = "books_schema"