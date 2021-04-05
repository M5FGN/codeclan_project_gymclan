from flask import Flask, render_template
from flask import Blueprint
from models.gymsession import Gymsession
import repositories.gymsession_repository as gymsession_repository

gymsessions_blueprint = Blueprint('gymsessions', __name__)

@gymsessions_blueprint.route('/gymsessions')
def gymsessions():
    gymsessions = gymsession_repository.view_all()
    return render_template('gymsessions/index.html', title='Sessions', gymsessions=gymsessions)

@gymsessions_blueprint.route('/gymsessions/<id>')
def view(id):
    gymsession = gymsession_repository.view(id)
    return render_template('gymsessions/gymsession.html', gymsession=gymsession)  
# TODO Add title Session Title

@gymsessions_blueprint.route('/gymsessions/add')
def add():
    return render_template('/gymsessions/add.html', title='Add a Session')

@gymsessions_blueprint.route('/gymsessions/edit')
def edit():
    return render_template('gymsessions/edit.html', title='Edit Session')

@gymsessions_blueprint.route('/gymsessions/delete')
def delete_gymsession():
    return render_template('gymsessions/delete.html', title='Delete Session')
