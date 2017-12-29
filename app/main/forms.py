from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField
from wtforms.validators import Email, DataRequired, EqualTo


class SignupForm(FlaskForm):
	first = StringField("First Name", validators=[DataRequired()])
	last = StringField("Last Name")
	email = StringField("Email", validators=[DataRequired(), Email()])
	dob = DateField("Date of Birth", format='%m/%d/%Y', validators=[DataRequired()])
	zipcode = IntegerField("Zipcode")
	phone = StringField("Phone Number")
	password = PasswordField("Password", validators=[DataRequired()])
	password2 = PasswordField("Re-enter Password", validators=[DataRequired(), EqualTo("password")])
	submit = SubmitField("Submit")


class LoginForm(FlaskForm):
	email = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Submit")


