from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField, PasswordField, FloatField
from wtforms.validators import DataRequired

class BMIForm(FlaskForm):
    weight = IntegerField()
    height = FloatField()

    submit = SubmitField()

class Registerform(FlaskForm):
    firstname = StringField(validators=[DataRequired()])
    lastname = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])

    submit = SubmitField()

class Loginform(FlaskForm):
    email = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])

    submit = SubmitField()

class CaloriesForm(FlaskForm):
    weight = IntegerField(validators=[DataRequired()])
    height = IntegerField(validators=[DataRequired()])
    age = IntegerField(validators=[DataRequired()])

    submit = SubmitField()

class ContactForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    message = StringField(validators=[DataRequired()])

    submit = SubmitField()