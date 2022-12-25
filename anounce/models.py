from anounce import db,app
from flask_login import UserMixin
from datetime import datetime
from flask_marshmallow import Marshmallow
import datetime



class anounce(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    date = db.Column(db.DateTime, nullable=False , default= datetime.datetime.now())
    voiture_id = db.Column(db.String(), db.ForeignKey('voiture.id'))
    
class voiture(db.Model, UserMixin):
    id =db.Column(db.Integer(),nullable=False, primary_key = True)
    marque = db.Column(db.String(20), nullable= False)
    modele = db.Column(db.String(20), nullable= False)
    anee = db.Column(db.Integer(), nullable= False)
    price = db.Column(db.Integer(), nullable= False)
    kilom = db.Column(db.Integer(), nullable= False)
    fuel = db.Column(db.String(20), nullable= False)
    seller_type = db.Column(db.String(20), nullable= False)
    transmission = db.Column(db.String(20), nullable= False)
    owner = db.Column(db.String(20), nullable= False)
    milleage = db.Column(db.Float(), nullable= False)
    engine = db.Column(db.Integer(), nullable= False)
    max_power = db.Column(db.Float(), nullable= False)
    seats = db.Column(db.Integer(), nullable= False)
    voitures = db.relationship('anounce', backref='voiture_id')
    
    
    
    
ma = Marshmallow(app)

class voitureschema(ma.Schema):
    class Meta:
        fields = ("id","marque", "modele" , "price" , "annee" , "kilom" , "fuel" , "seller_type" ,"transmission" , "owner" , "milleage" , "engine" , "max_power" ,"seats" )
       
voiture_schema = voitureschema()
voitures_schema = voitureschema(many =True) 

class anounceschema(ma.Schema):
    class Meta:
        fields = ("id","name","price")
        

anounce_schema = anounceschema()
anounces_schema = anounceschema(many =True)        
    
@app.before_first_request
def create_tables():
     db.create_all()
    
    
