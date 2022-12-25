from feedback import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from feedback.models import Feedback



class RegisterForm(FlaskForm):
    
    name = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Name"})
     
    email = StringField(validators=[
                           InputRequired(), Length(min=10, max=20)], render_kw={"placeholder": "email"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    
    phone = StringField(validators=[
                             InputRequired(), Length(min=10, max=10)], render_kw={"placeholder": "Phone"})

    submit = SubmitField('Register')

    


