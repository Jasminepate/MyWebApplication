from flask import render_template
from . import main

@main.errorhandler(400)
def page_not_found(e):
	return render_template("404.html"), 404

@main.errorhandler(500)
def interal_error(e):
	return render_template("500.html"), 500
