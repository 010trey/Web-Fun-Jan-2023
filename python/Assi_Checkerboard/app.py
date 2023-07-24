from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard_default():
    return render_checkerboard(8, 8)

@app.route('/<int:x>')
def checkerboard_x(x):
    return render_checkerboard(x, 8)

@app.route('/<int:x>/<int:y>')
def checkerboard_x_y(x, y):
    return render_checkerboard(x, y)

def render_checkerboard(rows, cols):
    return render_template('checkerboard.html', rows=rows, cols=cols)

if __name__ == '__main__':
    app.run(debug=True)
