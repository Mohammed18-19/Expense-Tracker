from app import app
from flask import render_template, url_for, request, make_response, redirect, flash
from datetime import date, datetime
from app import db
from app.models import Expense
import sqlalchemy as sa

CATEGORIES = ['Food', 'Transport', 'Rent', 'Utilities', 'Health']


@app.route("/")
def index():
    expenses = Expense.query.order_by(Expense.date.desc(), Expense.id.desc()).all()
    total = round(sum(e.amount for e in expenses), 2)
    return render_template('index.html', expenses=expenses, categories=CATEGORIES, total=total)


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
    
    try:
       d = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else date.today()
    except ValueError:
        d = date.today

    e = Expense(description=description, amount=amount, category=category, date=d)
    db.session.add(e)
    db.session.commit()

    flash('Expense added', "success")
    return redirect(url_for('index'))