# models.py - Database models and interactions; SQLite simulation
# PURPOSE - This file simulates interacting with a SQLite database to retrieve user and payroll data for the login and paycheck generation processes

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50))

    def __repr__(self):
        return f'<User {self.username}>'

# Define Payroll model
class Payroll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    tax_deductions = db.Column(db.Float, nullable=False)

    user = db.relationship('User', backref=db.backref('payrolls', lazy=True))

    def __repr__(self):
        return f'<Payroll for {self.username}>'

# Fetch user by username
def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

# Fetch payroll data for a user
def get_payroll_data(username):
    return Payroll.query.filter_by(username=username).first()
