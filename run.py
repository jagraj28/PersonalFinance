from flask import Flask, render_template, redirect, url_for, flash
from forms import add_assets, add_investments, add_debts, LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/assets', methods=['GET', 'POST'])
def assets():
    form = add_assets()
    if form.validate_on_submit():
        flash(f'Changes made saved!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Changes not saved, please check the data is correct!', 'danger')
    return render_template('assets.html', title='Assets', form=form)

@app.route('/investments', methods=['GET', 'POST'])
def investments():
    form = add_investments()
    if form.validate_on_submit():
        flash(f'Changes made saved!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Changes not saved, please check the data is correct!', 'danger')
    return render_template('investments.html', title='Investments', form=form)

@app.route('/debts', methods=['GET', 'POST'])
def debts():
    form = add_debts()
    if form.validate_on_submit():
        flash(f'Changes made saved!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Changes not saved, please check the data is correct!', 'danger')
    return render_template('debts.html', title='Debts', form=form)

if __name__ == '__main__':
    app.run(debug=True)