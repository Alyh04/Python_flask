from flask import request
from models.user import User
from extensions import db


def add_user_function():
    if request.method == "POST":
        nom=request.form['nom']
        prenom=request.form['prenom']
        email=request.form['email']
        numero=request.form['numero']
        statut=request.form['statut'] 
        user = User(
            nom=nom,
            prenom=prenom,
            email=email,
            numero=numero,
            statut=statut,
        )
        
        user.save()
        data = {
            'id_personne':user.id_personne,
            'nom':user.nom,
            'prenom':user.prenom,
            'email':user.email,
            'numero':user.numero,
            'statut':user.statut
        }
        return data 
    
def edit_user_function(user):
    if request.method == "POST":
        user.nom = request.form['nom']
        user.prenom = request.form['prenom']
        user.email = request.form['email']
        user.numero = request.form['numero']
        user.statut = request.form['statut']
        db.session.commit()
    return user

def delete_user_function(user):
    db.session.delete(user)
    db.session.commit()