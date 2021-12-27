from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Fan(db.Model):
    __tablename__ = 'fans'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column('First Name', db.String())
    lastname = db.Column('Last Name', db.String())
    email = db.Column('Email', db.String())
    birthdaymonth = db.Column('Birthday Month', db.String())

    def __repr__(self):
        return f'''<First Name: {self.firstname}
                    Last Name: {self.lastname}
                    Email: {self.email}
                    Birthday Month" {self.birthdaymonth}>'''