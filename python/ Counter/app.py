from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"   

@app.route('/')
def index():
    if 'visit_count' in session:
        session['visit_count'] += 1
    else:
        session['visit_count'] = 1
    return render_template('index.html', visit_count=session['visit_count'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
