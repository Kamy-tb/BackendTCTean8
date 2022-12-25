from user import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from user.models import User



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

    def validate_email(self, email):
        existing_user_email = User.query.filter_by(
            email=email.data).first()
        if existing_user_email:
            raise ValidationError(
                'That email already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField(validators=[
                           InputRequired(), Length(min=10, max=20)], render_kw={"placeholder": "email"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')
