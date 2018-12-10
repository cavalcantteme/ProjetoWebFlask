from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField("username", validators = [DataRequired()])
    password = PasswordField("password", validators = [DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField("name", validators = [DataRequired()])
    name = StringField("name", validators = [DataRequired()])
    email = StringField("email", validators = [DataRequired(),Email()])
    password = PasswordField("password", validators = [DataRequired()])

class SaleForm(FlaskForm):
    name = StringField("name", validators = [DataRequired()])
    adress = StringField("adress", validators = [DataRequired()])
    units = StringField("unit", validators = [DataRequired()])