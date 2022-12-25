from user import db,app
from flask_login import UserMixin
from datetime import datetime
from flask_marshmallow import Marshmallow
import datetime



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable = False, unique =True)
    password = db.Column(db.String(80), nullable=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    date = db.Column(db.String(), nullable=False , default= datetime.datetime.now())

ma = Marshmallow(app)

class userschema(ma.Schema):
    class Meta:
        fields = ("id","name","email","password")

user_schema = userschema()
users_schema = userschema(many =True)        
    
@app.before_first_request
def create_tables():
     db.create_all()
    
    
