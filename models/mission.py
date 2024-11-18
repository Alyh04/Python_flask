from extensions import db

class Mission(db.Model):
    __tablename__ = 'mission'

    id_mission = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    tache_a_faire = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False)
    statut_de_projet = db.Column(db.String(100), nullable=False)  # Rendre nullable=False
    financement = db.Column(db.String(100), nullable=False)  # Rendre nullable=False

    # Méthode __init__ correctement définie dans la classe
    def __init__(self, nom, tache_a_faire, date, statut_de_projet='non défini', financement='non défini'):
        self.nom = nom
        self.tache_a_faire = tache_a_faire
        self.date = date
        self.statut_de_projet = statut_de_projet
        self.financement = financement

# Fonction pour ajouter une mission dans la base de données
def ajouter_mission(nom, tache_a_faire, date, statut_de_projet='non défini', financement='non défini'):
    mission = Mission(nom, tache_a_faire, date, statut_de_projet, financement)
    db.session.add(mission)
    db.session.commit()
