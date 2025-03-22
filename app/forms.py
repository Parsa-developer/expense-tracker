from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, NumberRange

class ExpenseForm(FlaskForm):
    amount = FloatField('Amount', validators=[
        DataRequired(),
        NumberRange(min=0.01, message="Amount must be greater than 0")
    ])
    category = SelectField('Category', choices=[
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Housing', 'Housing'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other')
    ], validators=[DataRequired()])
    description = TextAreaField('Description')