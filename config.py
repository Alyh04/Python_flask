import os

class Config: 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/projet_fid' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Ajouter la clé secrète pour gérer les sessions Flask
    SECRET_KEY = os.urandom(24)  # Génère une clé secrète aléatoire de 24 octets
