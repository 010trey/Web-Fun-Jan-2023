from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'number' not in session:
        # Generate a random number between 1 and 100 and store it in the session
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0

    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1

        if guess < session['number']:
            message = "Too low. Try again!"
        elif guess > session['number']:
            message = "Too high. Try again!"
        else:
            message = "Congratulations! You guessed the correct number. Play again!"
            session.pop('number')  # Clear the number from the session to start a new game
            session.pop('attempts')

        return render_template('index.html', message=message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
