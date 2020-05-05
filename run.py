from flask import Flask, render_template, redirect, url_for, flash
from forms import add_assets, add_investments, add_debts
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class adding_assets(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    bank = db.Column(db.String(30), unique=False, nullable=False)
    amount = db.Column(db.Integer, unique=False, nullable=False)
    interest = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"adding_assets('{self.bank}', '{self.amount}', '{self.interest}')"


class adding_investments(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(30), unique=False, nullable=False)
    amount = db.Column(db.Integer, unique=False, nullable=False)
    growth = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"adding_investments('{self.institution}', '{self.amount}', '{self.growth}')"


class adding_debts(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    debt_type = db.Column(db.String(30), unique=False, nullable=False)
    amount = db.Column(db.Integer, unique=False, nullable=False)
    interest = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"adding_debts('{self.debt_type}', '{self.amount}', '{self.interest}')"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/assets', methods=['GET', 'POST'])
def assets():
    form = add_assets()
    if form.validate_on_submit():
        asset = adding_assets(bank=form.bank.data, amount=form.amount.data, interest=form.interest.data)
        db.session.add(asset)
        db.session.commit()
        flash(f'Changes made saved!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Changes not saved, please check the data is correct!', 'danger')
    return render_template('assets.html', title='Assets', form=form)


@app.route('/investments', methods=['GET', 'POST'])
def investments():
    form = add_investments()
    if form.validate_on_submit():
        investment = adding_investments(institution=form.institution.data, amount=form.amount.data, growth=form.growth.data)
        db.session.add(investment)
        db.session.commit()
        flash(f'Changes made saved!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Changes not saved, please check the data is correct!', 'danger')
    return render_template('investments.html', title='Investments', form=form)


@app.route('/debts', methods=['GET', 'POST'])
def debts():
    form = add_debts()
    if form.validate_on_submit():
        debt = adding_debts(debt_type=form.debt_type.data, amount=form.amount.data, interest=form.interest.data)
        db.session.add(debt)
        db.session.commit()
        flash(f'Changes made saved!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Changes not saved, please check the data is correct!', 'danger')
    return render_template('debts.html', title='Debts', form=form)


@app.route('/account', methods=['GET', 'POST'])
def account():
    form_1 = adding_assets.query.all()
    form_2 = adding_investments.query.all()
    form_3 = adding_debts.query.all()
    result_1 = [r.amount for r in db.session.query(adding_assets).all()]
    result_2 = [r.amount for r in db.session.query(adding_investments).all()]
    total_assets = sum(result_1) + sum(result_2)
    result_3 = [r.amount for r in db.session.query(adding_debts).all()]
    total_debts = sum(result_3)
    return render_template('account.html', title='Account', form_1=form_1, form_2=form_2, form_3=form_3, 
                            total_assets=total_assets, total_debts=total_debts)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    return render_template('edit.html', title='Edit')


if __name__ == '__main__':
    app.run(debug=True)