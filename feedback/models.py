from feedback import db , app
from flask_login import UserMixin
from datetime import datetime
from flask_marshmallow import Marshmallow
import datetime

class Annonce (db.Model) :
    id = db.Column(db.Integer() , primary_key=True)
    #date = db.Column(db.Date(), nullable=False , default= datetime.datetime.now().strftime("%H:%M:%S"))
    favoris = db.Column(db.Integer())
    #feedback = db.relationship('Feedback', backref='feedbackAnnonce')



class Voiture (db.Model) :
    id = db.Column(db.Integer() , primary_key=True)
    name = db.Column(db.String(length=300) )
    modele = db.Column(db.String(length=300) )
    km_driven = db.Column(db.Integer())
    transmission = db.Column(db.String(length=30) ) 
    annee = db.Column(db.Integer())
    siege = db.Column(db.Integer())





class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable = False, unique =True)
    password = db.Column(db.String(80), nullable=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    #feedback = db.relationship('Feedback', backref='feedback',)
    date = db.Column(db.Date(), nullable=False , default= datetime.datetime.now().strftime("%H:%M:%S"))

ma = Marshmallow(app)

class Feedback(db.Model) :
    id = db.Column(db.Integer() , primary_key=True)
    text = db.Column(db.String(length=300) )
    #annonce_id = db.Column(db.Integer() , db.ForeignKey('annonce.id'))

class feedbackschema(ma.Schema):
    class Meta:
        fields = ("id","text","annonce_id","user_id")

feedback_schema = feedbackschema()
feedback_schema = feedbackschema(many =True)        
    
class Annonceschema(ma.Schema):
    class Meta:
        fields = ("id" , "date","favoris")
        
annonce_schema = Annonceschema()
annonce_schema = Annonceschema(many =True)    

    
    
