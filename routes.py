from flask import Blueprint, flash, redirect ,render_template, request, url_for
from controllers.mission import add_mission_function, edit_mission_function
from controllers.users import add_user_function,edit_user_function,delete_user_function
import sys
from models.mission import Mission
from models.user import User
from extensions import db

main = Blueprint('main', __name__) #nome du root = name

@main.route('/',methods=['GET'])
def home():
    data = User.get_all() 
    return render_template('index.html', data=data)

@main.route('/personne', methods=['GET'])
def personne():
    data = User.get_all()
    return render_template('personne.html', data=data)

@main.route('/adduser', methods=['GET', 'POST'])
def add_user():
    if request.method == "POST":
        data = add_user_function() 
        print(data, file=sys.stderr)
        return redirect(url_for('main.personne')) 
    return render_template('personne_ajouter.html')

@main.route('/edituser/<int:id_personne>', methods=['GET', 'POST'])
def edit_user(id_personne):
    user = User.query.get_or_404(id_personne) 
    if request.method == 'POST':
        user = edit_user_function(user)
        flash("Les informations ont été mises à jour avec succès !", "success")
        return redirect(url_for('main.personne')) 
    return render_template('personne_modifier.html', user=user)

@main.route('/deleteuser/<int:id_personne>', methods=['POST'])
def delete_user(id_personne):
    user = User.query.get_or_404(id_personne)
    delete_user_function(user)  # La fonction de suppression
    return redirect(url_for('main.personne'))



@main.route('/mission')
def mission():
    data = Mission.query.all()
    print(data)  # Inspectez les données
    return render_template('mission.html', data=data)


@main.route('/addmission', methods=['GET', 'POST'])
def add_mission():
    if request.method == "POST":
        nom = request.form['nom']
        tache_a_faire = request.form['tache_a_faire']
        date = request.form['date']
        statut_de_projet = request.form.get('statut_de_projet')
        financement = request.form.get('financement')  
        add_mission_function(nom, tache_a_faire, date, statut_de_projet, financement)
        flash("Mission ajoutée avec succès !", "success")
        return redirect(url_for('main.mission'))
    personnes = User.query.all()
    return render_template('mission_ajouter.html', personnes=personnes)




@main.route('/editmission/<int:id_mission>', methods=['GET', 'POST'])
def edit_mission(id_mission):
    mission = Mission.query.get_or_404(id_mission)
    if request.method == 'POST':
        mission = edit_mission_function(mission)
        flash("La mission a été mise à jour avec succès !", "success")
        return redirect(url_for('main.mission'))
    return render_template('mission_modifier.html', mission=mission)

@main.route('/deletemission/<int:id_mission>', methods=['POST'])
def delete_mission(id_mission):
    mission = Mission.query.get_or_404(id_mission)
    db.session.delete(mission)
    db.session.commit()
    
    flash("Mission supprimée avec succès !", "success")
    return redirect(url_for('main.mission'))

