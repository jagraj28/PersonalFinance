from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

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