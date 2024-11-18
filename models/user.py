from extensions import db


class User(db.Model):
    __tablename__ = 'personnel'
    id_personne = db.Column(db.Integer,primary_key=True)
    nom = db.Column(db.String(80),nullable=False,unique=True)
    prenom = db.Column(db.String(200),nullable=False,unique=True)
    email = db.Column(db.String(200),nullable=False,unique=True)
    numero = db.Column(db.String(200))
    statut = db.Column(db.DateTime(),nullable=True,server_default=db.func.new())

    @property
    def data (self):
        return{
            'id_personne':self.id_personne,
            'nom':self.nom,
            'prenom':self.prenom,
            'email':self.email,
            'numero':self.numero,
            'statut':self.statut,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
        
    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result = []
        
        for i in r:
            result.append(i.data)
        return result 
    
    @classmethod
    def get_by_id(cls,id_personne):
        return cls.query.filter(cls.id_personne == id_personne).first()