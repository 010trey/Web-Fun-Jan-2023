from flask import render_template, request, redirect
from flask_app.models.quote import Quote
from flask_app import app

#===================GET ALL ================
@app.route('/')
def index():
    quotes_list = Quote.get_all()
    return render_template('index.html', quotes=quotes_list)

# =================GET ONE BY ID====================
@app.route('/quotes/<int:quote_id>')
def one_quote(quote_id):
    one_quote = Quote.get_by_id({'id':quote_id})
    return render_template("one_quote.html", quote = one_quote)

# ==================CREATE====================
@app.route('/quotes/new')
def new_quote():
    return render_template("new_quote.html")

@app.route('/quotes/create', methods=["POST"])
def create():
    # print(request.form)
    Quote.create(request.form)
    return redirect('/')

# ==================UPDATE====================
@app.route('/quotes/<int:quote_id>/edit')
def edit_quote(quote_id):
    one_quote = Quote.get_by_id({'id': quote_id})
    return render_template("edit_quote.html", quote = one_quote)

@app.route('/quotes/<int:quote_id>/update', methods=["POST"])
def update(quote_id):
    print(request.form)
    data = {
        **request.form,
        'id':quote_id
    }
    Quote.update(data)
    return redirect('/')

# =========================DELETE + DESTROY ==================
@app.route('/quotes/<int:quote_id>/destroy', methods=['POST'])
def destroy(quote_id):
    Quote.destroy({'id':quote_id})
    return redirect('/')