from flask import url_for,render_template,redirect
from anounce import app,db
from anounce.models import anounce, anounces_schema
from anounce.form import voitureForm ,searchForm

@app.get('/getallanounces')
def getanounce():
    anounces = anounce.query.order_by(anounce.id.desc(),anounce.date).all()
    return anounces_schema.dump(anounces)


@ app.route('/formulaire', methods=['GET', 'POST'])
def formulaire():
    form = voitureForm()

    if form.validate_on_submit():
        new_anounce = anounce(marque=form.marque.data,modele=form.modele.data,anee=form.anee.data,price=form.price.data,kilom=form.kilom.data,fuel=form.fuel.data,seller_type=form.seller_type.data,transmission=form.transmission.data,owner=form.owner.data,milleage=form.milleage.data,engine=form.engine.data,max_power=form.max_power.data,seats=form.seats.data)
        db.session.add(new_anounce)
        db.session.commit()
        return redirect(url_for('getallanounce'))

    return render_template('formulaire.html', form=form)

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
    
        
