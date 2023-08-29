from flask import Flask

# file upload
# from config import Config

app = Flask(__name__)
app.secret_key = "Adouma shhhhhhh!!"
DB = "py_project"

UPLOAD_FOLDER = "D:/coding dojo/coding_dojo_projects/Python-Project/speedyserv/static/img/uploads/"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# file upload
# app.config.from_object(Config)

