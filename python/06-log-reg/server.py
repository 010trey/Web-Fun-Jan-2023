from flask_app import app

# ! CONTROLLERS HERE
from flask_app.controllers import users


if __name__ == '__main__':
    app.run(debug=True, port=5003)