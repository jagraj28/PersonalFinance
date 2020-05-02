from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/assets/')
def assets():
    return render_template('assets.html')

@app.route('/investments/')
def investments():
    return render_template('investments.html')

@app.route('/debts/')
def debts():
    return render_template('debts.html')

if __name__ == '__main__':
    app.run(debug=True)