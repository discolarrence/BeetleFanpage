from flask import Flask, render_template, url_for, request
from models import db, app, Fan
import time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contests')
def contests():
    return render_template('contests.html')

@app.route('/beetle-care')
def beetle_care():
    return render_template('beetle-care.html')

@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.form:
        new_fan = Fan(firstname=request.form['firstname'], 
                    lastname = request.form['lastname'],
                    email = request.form['email'],
                    birthdaymonth = request.form['birthdaymonth'],
                    favoritebeetle = request.form['favoritebeetle'])
        db.session.add(new_fan)
        db.session.commit()
        time.sleep(5)
        return render_template('signup.html')
    else:
        return render_template('signup.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')