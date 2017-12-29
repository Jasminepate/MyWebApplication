from datetime import datetime
from flask import render_template, request, url_for, session, flash, redirect
from flask import send_from_directory
from flask_login import login_user
from sqlalchemy import exc

from . import main
from .forms import SignupForm, LoginForm
from .scripts import HashPass
from .. import db
from ..models import User

@main.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@main.route("/login", methods=["GET", "POST"])
def login():
	form = SignupForm()
	email = form.email.data
	password = form.password.data
	user = User.query.filter_by(email=form.email.data).first()
	access = None
	if "submit" in request.form:
		if user is None:
			access = "Register"
		else:
			process = HashPass(user.password, password)
			result = process.verify()
			if result is True:
				login_user(user)
				session["user"] = user.first_name + user.last_name
				access = "Granted"
				user.last_login = datetime.now()
				db.session.add(user)
				db.session.commit() 
				return redirect(url_for("auth.access"))
			else:
				access = "Denied"
	if "register_submit" in request.form and form.validate_on_submit():
		try:
			user = User.query.filter_by(email=form.email.data).first()
			if user is None:
				first  = form.first.data
				last = form.last.data
				email = form.email.data
				dob = form.dob.data
				zipcode = form.zipcode.data
				phone = form.phone.data
				password = form.password.data

				process = HashPass(password)
				hashed_password = process.hashit()
				new_user = User(first_name=first, last_name=last, email=email, dob=dob, zipcode=zipcode, phone=phone,  password=hashed_password, last_login=datetime.now())
				db.session.add(new_user)
				db.session.commit()
				login_user(new_user)
		except exc.IntegrityError:
			db.session().rollback()
		return redirect(url_for("auth.access"))
	return render_template("login.html", form=form, access=access)


@main.route('/static/<filename>')
def send_static(filename):
    return send_from_directory('static', filename)
