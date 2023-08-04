from flask_app import app

# ! Import ALL CONTROLLERS HERE 🚫⛔
from flask_app.controllers import authors, books

if __name__ == '__main__':
    app.run(debug = True, port=5001)