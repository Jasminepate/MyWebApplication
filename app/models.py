from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from . import db, login

class User(UserMixin, db.Model):
	__tablename__ = "registered_users"
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(64))
	last_name = db.Column(db.String(64))
	email = db.Column(db.String(255))
	dob = db.Column(db.Date)
	zipcode = db.Column(db.Integer)
	phone = db.Column(db.String(64))
	last_login = db.Column(db.DateTime())
	password = db.Column(db.String(255))
	
	def __repr__(self):
		return "<name %r>" % self.name

@login.user_loader
def user(user_id):
	return User.query.get(int(user_id))


