from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextField, SubmitField
from wtforms.validators import DataRequired

class add_assets(FlaskForm):
    bank = TextField('Bank', validators=[DataRequired()])
    amount = StringField('Amount', validators=[DataRequired()])
    interest = StringField('Interest', validators=[DataRequired()])
    submit = SubmitField('Save changes')

class add_investments(FlaskForm):
    institution = TextField('Institution', validators=[DataRequired()])
    amount = StringField('Amount', validators=[DataRequired()])
    growth = StringField('Growth', validators=[DataRequired()])
    interest = StringField('Interest', validators=[DataRequired()])
    submit = SubmitField('Save changes')

class add_debts(FlaskForm):
    debt_type = TextField('Type', validators=[DataRequired()])
    amount = StringField('Amount', validators=[DataRequired()])
    interest = StringField('Interest', validators=[DataRequired()])
    submit = SubmitField('Save changes')