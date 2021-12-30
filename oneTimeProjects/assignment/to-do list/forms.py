from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, length, Email


class RegistrationForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    passwd = PasswordField("Password", validators=[DataRequired(),
                                                   length(min=8, message="Should Be Atleast 8 Characters")])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    passwd = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

