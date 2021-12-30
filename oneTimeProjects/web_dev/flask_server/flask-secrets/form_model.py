from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class MyForm(FlaskForm):
    mail = StringField(label="Email :", validators=[DataRequired(), Email(message="Enter Correct Mail")])
    passwd = PasswordField(label="Password :",
                           validators=[
                               DataRequired(),
                               Length(min=8, message="atleast 8 Characters")])
    sub = SubmitField(label="Submit")
