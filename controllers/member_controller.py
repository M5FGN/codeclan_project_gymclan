from flask import Flask, render_template
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def members():
    members = member_repository.view_all()
    return render_template('members/index.html', title='Members', members=members)

@members_blueprint.route('/members/<id>')
def view(id):
    member = member_repository.view(id)
    return render_template('members/member.html', member=member)  
# TODO Add title Members Name

@members_blueprint.route('/members/add')
def add():
    return render_template('members/add.html', title='Add New Member')

@members_blueprint.route('/members/edit')
def edit():
    return render_template('members/edit.html', title='Edit Member')

@members_blueprint.route('/members/delete')
def delete_member():
    return render_template('members/delete.html', title='Delete Member')