from flask_app import app

# ! Don't forget to import all controllers here 
from flask_app.controllers import artists_controller


if __name__ == '__main__':
    app.run(debug=True, port=5001)