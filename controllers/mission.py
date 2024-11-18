from flask import request
from models.mission import Mission
from extensions import db

def add_mission_function(nom, tache_a_faire, date, statut_de_projet=None, financement=None):
    if not statut_de_projet:
        statut_de_projet = 'Pas défini'  # Par exemple, une valeur par défaut
    if not financement:
        financement = 'Pas défini'  # Par exemple, une valeur par défaut

    mission = Mission(
        nom=nom,
        tache_a_faire=tache_a_faire,
        date=date,
        statut_de_projet=statut_de_projet,
        financement=financement
    )
    
    db.session.add(mission)
    db.session.commit()
    
    data = {
        'id_mission': mission.id_mission,
        'nom': mission.nom,
        'tache_a_faire': mission.tache_a_faire,
        'date': mission.date,
        'statut_de_projet': mission.statut_de_projet,
        'financement': mission.financement
    }
    
    return data



def edit_mission_function(mission):
    """
    Cette fonction édite une mission existante. Elle met à jour les champs de la mission
    avec les valeurs envoyées par le formulaire. Si un champ est manquant, la valeur existante est conservée.
    """
    if request.method == "POST":
        mission.nom = request.form['nom']
        mission.tache_a_faire = request.form['tache_a_faire']
        mission.date = request.form['date']
        mission.statut_de_projet = request.form.get('statut_de_projet', mission.statut_de_projet)  # Utilise la valeur existante si None
        mission.financement = request.form.get('financement', mission.financement)  # Utilise la valeur existante si None
        db.session.commit()
    return mission


def delete_mission_function(mission):
    """
    Cette fonction supprime une mission de la base de données.
    """
    db.session.delete(mission)
    db.session.commit()
