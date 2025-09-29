from app import app
from flask import render_template, url_for, request, make_response, flash, redirect


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/add", methods=['POST'])
def add():

    description = request.form.get('description', "").strip()
    amount_str = request.form.get('amount', "").strip()
    category = request.form.get('category', "").strip()
    date_str = request.form.get('date', "").strip()

    if not description or not amount_str or not category:
        flash("Please fill description, amount, and category", "error")
        return redirect(url_for('index'))

    try: # Try the code and handle errors if any
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError
    except ValueError: # raise the Error if it's
        flash('Amount must be a positive number', 'error')
        return redirect(url_for('index'))

    print("Form received:", dict(request.form))
    return make_response("Form received check the console")
