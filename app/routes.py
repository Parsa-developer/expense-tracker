from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Expense
from app.forms import ExpenseForm
from app import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    total = sum(expense.amount for expense in expenses)
    category_totals = {}
    for expense in expenses:
        category_totals[expense.category] = category_totals.get(expense.category, 0) + expense.amount
    return render_template('index.html', 
                         expenses=expenses,
                         total=total,
                         category_totals=category_totals)

@main.route('/add', methods=['GET', 'POST'])
def add_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        expense = Expense(
            amount=form.amount.data,
            category=form.category.data,
            description=form.description.data
        )
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_expense.html', form=form)

@main.route('/delete/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/categories')
def manage_categories():
    return render_template('categories.html')