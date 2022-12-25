from flask import url_for,render_template,redirect,request
from anounce import app,db
from anounce.models import anounce, anounces_schema,voiture
from anounce.form import voitureForm ,searchForm

@app.get('/getallanounces')
def getanounce():
    anounces = anounce.query.order_by(anounce.id.desc(),anounce.date).all()
    return anounces_schema.dump(anounces)


@ app.route('/formulaire', methods=['GET', 'POST'])
def formulaire():
    if request.method == 'POST':
        marque = request.json['marque']
        modele = request.json['modele']
        anee = request.json['anee']
        kilom = request.json['kilom']
        fuel = request.json['fuel']
        seller_type = request.json['seller_type']
        transmission = request.json['transmission']
        owner = request.json['owner']
        milleage = request.json['milleage']
        engine = request.json['engine']
        max_power = request.json['ax_power']
        seats = request.json['seats']

        new_voiture = voiture(marque,modele,anee,kilom,fuel,seller_type,transmission,owner,milleage,engine,max_power,seats)
        db.session.add(new_voiture)
        db.session.commit()
        if (new_voiture): return ('added successfully') 

import joblib
clf = joblib.load('./finalized_model_TC.sav')
@app.route('/prediction<id_user>' , methods = ['POST'])
def calcul_prix(id_user):
    marque = request.json['marque']
    modele = request.json['modele']
    anee = request.json['anee']
    kilom = request.json['kilom']
    fuel = request.json['fuel']
    seller_type = request.json['seller_type']
    transmission = request.json['transmission']
    owner = request.json['owner']
    milleage = request.json['milleage']
    engine = request.json['engine']
    max_power = request.json['ax_power']
    seats = request.json['seats']
    table = [[anee ,kilom, fuel , seller_type , transmission , owner , milleage , engine , max_power , seats , marque , modele]]
    prediction_price = clf.predict(table)
    

@app.context_processor
def base():
     form =searchForm()
     return dict(form=form)


@app.route('/search', methods=["POST"])
def search():
    form = searchForm()
    
    if form.validate_on_submit():
        anounce.searched = form.searched.data
        anounce = anounce.filter(anounce.vehicle_id.modele.like('%'+ anounce.searched + '%')) 
        anounce = anounce.order_by(anounce.vehicle_id.price)
        return render_template('search.html',form=form,searched = anounce.searched)
    
        
