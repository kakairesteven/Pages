from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
# from ..models import User


class RegistrationForm(Form):
    email = StringField('email', validators=[DataRequired(), Length(max=45)])
    surname = StringField('surname', validators=[DataRequired(), Length(max=45)])
    first_name = StringField('first_name', validators=[DataRequired(), Length(max=45)])
    date_of_birth = DateTimeField('date_of_birth', validators=[DataRequired(), Length(max=45)])
    country = StringField('country', validators=[DataRequired(), Length(max=60)])
    submit_form = SubmitField('submit')
    
    
class signInForm(Form):
    email = StringField('email', validators=[DataRequired(), Length(max=45)])
    password = StringField('password')
    submit_form = SubmitField('submit')

