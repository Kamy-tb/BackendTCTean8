from anounce import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from anounce.models import anounce



class voitureForm(FlaskForm):
    
    marque = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "marque"})
     
    modele = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "modele "})

    anee = StringField(validators=[
                             InputRequired(), Length(min=4, max=6)], render_kw={"placeholder": "anee"})
    
    price = StringField(validators=[
                             InputRequired(), Length(min=10, max=10)], render_kw={"placeholder": "price"})
    
    kilom = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "kilom"})
     
    fuel = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "fuel"})

    seller_type  = StringField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "seller_type"})
    
    transmission  = StringField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "transmission"})
    
    owner = StringField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "owner"})
    
    milleage = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "milleage"})

    engine  =  StringField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "engine"})
    
    max_power  = StringField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "max_power"})
    
    seats  = StringField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "seats"})
    
    

    submit = SubmitField('Submit')
    

class searchForm(FlaskForm):
    StringField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "search"})