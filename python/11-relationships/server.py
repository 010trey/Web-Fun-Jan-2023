from flask_app import app

# ! CONTROLLERS HERE 🚫⛔
from flask_app.controllers import authors, quotes
if __name__ == '__main__':
    app.run(debug=True, port=5002) 