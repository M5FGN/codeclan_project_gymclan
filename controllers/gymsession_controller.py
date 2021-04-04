from flask import Flask, render_template
from flask import Blueprint
from models.gymsession import Gymsession
import repositories.gymsession_repository as gymsession_repository

gymsessions_blueprint = Blueprint('gymsessions', __name__)

@gymsessions_blueprint.route('/gymsessions')
def gymsessions():
    gymsessions = gymsession_repository.view_all()
    return render_template('gymsessions/index.html', title='Sessions', gymsessions=gymsessions)

