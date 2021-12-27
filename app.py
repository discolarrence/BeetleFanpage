from flask import Flask, render_template, url_for
from models import db, app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contests')
def contests():
    return render_template('contests.html')

@app.route('/beetle-care')
def beetle_care():
    return render_template('beetle-care.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')