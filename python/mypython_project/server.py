from flask_app import app

from flask_app.controllers import user
from flask_app.controllers import product


if __name__ == '__main__':
    app.run(debug = True)