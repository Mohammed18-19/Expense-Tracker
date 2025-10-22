from app import app
from flask import render_template, url_for, request, redirect, flash
from datetime import date, datetime
from app import db
from app.models import Expense
from sqlalchemy import func

CATEGORIES = ['Food', 'Transport', 'Rent', 'Utilities', 'Health']

def parse_date_or_none(s: str):
    if not s:
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return None


@app.route("/")
def index():

    start_str = (request.args.get("start") or "").strip()
    end_str = (request.args.get("end") or "").strip()
    selected_category = (request.args.get("category") or "").strip()

    start_date = parse_date_or_none(start_str)
    end_date = parse_date_or_none(end_str)

    if start_date and end_date and end_date < start_date:
        flash("End date cannot be before start date", "error")
        start_date = end_date = None
        start_str = end_str = ""

    q = Expense.query
    if start_date:
        q = q.filter(Expense.date >= start_date)
    if end_date:
        q = q.filter(Expense.date <= end_date)
    
    if selected_category:
        q = q.filter(Expense.category == selected_category)


    expenses = q.order_by(Expense.date.desc(), Expense.id.desc()).all()
    total = round(sum(e.amount for e in expenses), 2)

# pie chart
    cat_q = db.session.query(Expense.category, func.sum(Expense.amount))
    
    if start_date:
        cat_q = cat_q.filter(Expense.date >= start_date)
    if end_date:
        cat_q = cat_q.filter(Expense.date <= end_date)
    if selected_category:
        cat_q = cat_q.filter(Expense.date == selected_category)

    cat_rows = cat_q.group_by(Expense.category).all()
    cat_labels = [c for c, _ in cat_rows]
    cat_values = [round(float(s or 0), 2) for _, s in cat_rows]

# day chart
    
    day_q = db.session.query(Expense.date, func.sum(Expense.amount))

    if start_date:
        day_q = day_q.filter(Expense.date >= start_date)
    if end_date:
        day_q = day_q.filter(Expense.date <= end_date)
    if selected_category:
        day_q = day_q.filter(Expense.date == selected_category)

    day_rows = day_q.group_by(Expense.category).order_by(Expense.date).all()
    day_labels = [d.isoformat() for d, _ in day_rows]
    day_values = [round(float(s or 0), 2) for _, s in day_rows]

    return render_template(
        'index.html', expenses=expenses, categories=CATEGORIES, total=total, start_str=start_str, end_str=end_str, today=date.today().isoformat(),
        selected_category=selected_category, cat_values=cat_values, cat_labels=cat_labels, day_labels=day_labels, day_values=day_values)


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


@app.route("/delete/<int:expense_id>", methods=['POST'])
def delete(expense_id):
    e = Expense.query.get_or_404(expense_id)
    db.session.delete(e)
    db.session.commit()
    flash('Expense deleted', 'success')
    return redirect(url_for('index'))