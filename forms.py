from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class add_assets(FlaskForm):
    bank = TextField('Bank', validators=[DataRequired()])
    amount = StringField('Amount (£)', validators=[DataRequired()])
    interest = StringField('Interest (%)', validators=[DataRequired()])
    submit = SubmitField('Save changes')

class add_investments(FlaskForm):
    institution = TextField('Institution', validators=[DataRequired()])
    amount = StringField('Amount (£)', validators=[DataRequired()])
    growth = StringField('Growth (%)', validators=[DataRequired()])
    submit = SubmitField('Save changes')

class add_debts(FlaskForm):
    debt_type = TextField('Type', validators=[DataRequired()])
    amount = StringField('Amount (£)', validators=[DataRequired()])
    interest = StringField('Interest (%)', validators=[DataRequired()])
    submit = SubmitField('Save changes')

class edit_assets(FlaskForm):
    amount = StringField('Amount (£)', validators=[DataRequired()])
    interest = StringField('Interest (%)', validators=[DataRequired()])
    submit = SubmitField('Save changes')

class edit_investments(FlaskForm):
    amount = StringField('Amount (£)', validators=[DataRequired()])
    growth = StringField('Growth (%)', validators=[DataRequired()])
    submit = SubmitField('Save changes')

class edit_debts(FlaskForm):
    amount = StringField('Amount (£)', validators=[DataRequired()])
    interest = StringField('Interest (%)', validators=[DataRequired()])
    submit = SubmitField('Save changes')