from flask_app import app

from flask_app.controllers import user
from flask_app.controllers import band


if __name__ == '__main__':
    app.run(debug = True)