from feedback import app, db
from flask import Flask, render_template, url_for, redirect, jsonify , request
#from feedback.form import LoginForm, RegisterForm
from feedback.models import Feedback , feedback_schema , Annonce , annonce_schema

@app.route('/')
def home():
    return "hi"


@app.get('/getallfeedbacks')
def getfeedbacks():
    all = Feedback.query.all()
    return feedback_schema.dump(all)

@app.get('/getfavories')
def getfavories():
    allF = Annonce.query.filter_by(favoris=1).all()
    return annonce_schema.dump(allF)

@app.post('/addfeedback')
def add_feedback():
  text = request.json['text']
  annonce_id = request.json['annonce_id']
  user_id = request.json['user_id']
  new = Feedback(text , annonce_id , user_id )
  db.session.add(new)
  db.session.commit()

@app.put('/changefavoriestate/<id>')
def changefavorietate(id):
    a = Annonce.query.get(id)
    if (a.favoris) :
        a.favoris = 0
    else :
        a.favoris = 1
    a.favoris  
    db.session.commit()
    return annonce_schema.jsonify(a)
 


@app.route('/prediction<id_user>' , methods = ['POST'])
def calcul_prix(id_user):
    year = request.json['year']
    km_driven = request.json['km_driven']
    fuel = request.json['fuel']
    seller_type = request.json['seller_type']
    transmission = request.json['transmission']
    owner = request.json['owner']
    mileage = request.json['mileage']
    engine = request.json['engine']
    max_power = request.json['max_power']
    seats = request.json['seats']
    marque = request.json['marque']
    model = request.json['model']
    table = [[year ,km_driven, fuel , seller_type , transmission , owner , mileage , engine , max_power , seats , marque , model]]
    prediction_price = clf.predict(table)
    
    
    
    



     
        


