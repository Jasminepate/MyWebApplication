from datetime import datetime
from flask import render_template, session, url_for, flash, redirect, request
from flask_login import login_required, logout_user
from werkzeug.datastructures import ImmutableMultiDict
from . import auth
from .forms import UserForm
from ..models import User

@auth.route("/access", methods=["GET", "POST"])
@login_required
def access():
	form = UserForm()
	print(request.args)
	print(dict(request.form))
	return render_template("access.html", form=form)

@auth.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
	logout_user()
	flash("You have successfully logged off")
	return redirect(url_for("main.login"))

@auth.route("/static/<filename>", methods=["GET", "POST"])
def send_static(filename):
	return send_from_directory("static", filename)


