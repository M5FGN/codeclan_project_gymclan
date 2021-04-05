from flask import Flask, render_template, redirect, request
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
    return render_template('gymsessions/gymsession.html', title='Session Details', gymsession=gymsession)  
# TODO Add title Session Title

@gymsessions_blueprint.route('/gymsessions/add')
def add():
    return render_template('/gymsessions/add.html', title='Add New Session')

@gymsessions_blueprint.route('/gymsessions/add_gymsession', methods=['POST'])
def add_gymsession():
    gs_title = request.form['gs_title']
    gs_description = request.form['gs_description']
    gs_type = request.form['gs_type']
    ability_level = request.form['ability_level']
    gs_day = request.form['gs_day']
    gs_date = request.form['gs_date']
    gs_time = request.form['gs_time']
    duration = request.form['duration']
    gs_plan = request.form['gs_plan']
    gs_location = request.form['gs_location']
    cost = request.form['cost']
    capacity = request.form['capacity']
    instructor = request.form['instructor']
    gymsession = Gymsession(gs_title, gs_description, gs_type, ability_level, gs_day, gs_date, gs_time, duration, gs_plan, gs_location, cost, capacity, instructor)
    gymsession_repository.save(gymsession)
    return redirect('/gymsessions')

@gymsessions_blueprint.route('/gymsessions/edit')
def edit():
    return render_template('gymsessions/edit.html', title='Edit Session')

@gymsessions_blueprint.route('/gymsessions/<id>/delete')
def delete_gymsession(id):
    gymsession = gymsession_repository.view(id)
    return render_template('gymsessions/delete.html', title='Delete Session', gymsession=gymsession)

@gymsessions_blueprint.route('/gymsessions/<id>/delete_confirmation')
def delete_gymsession_save(id):
    gymsession_repository.delete_gymsession(id)
    return redirect('/gymsessions')
