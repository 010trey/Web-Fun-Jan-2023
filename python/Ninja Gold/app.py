from flask import Flask, render_template, request,session 
import random

app = Flask(__name__)
app.secret_key = "secret_key" 


@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0
        session["activities"] = []
    return render_template("index.html")


@app.route("/process_money", methods=["POST"])
def process_money():
    buildings = {
        "farm": {"min_gold": 10, "max_gold": 20},
        "cave": {"min_gold": 5, "max_gold": 10},
        "house": {"min_gold": 2, "max_gold": 5},
        "casino": {"min_gold": -50, "max_gold": 50},
    }

    building = request.form["building"]
    earnings = random.randint(buildings[building]["min_gold"], buildings[building]["max_gold"])

    session["gold"] += earnings

    if earnings >= 0:
        activity = f"Earned {earnings} gold from the {building}!"
    else:
        activity = f"Entered a casino and lost {-earnings} gold... Ouch..."

    session["activities"].append(activity)

    return index()  # Redirect to the root route to display the updated information


if __name__ == "__main__":
    app.run(debug=True)
