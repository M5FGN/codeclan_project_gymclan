from flask import Flask, render_template, redirect, request
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

@members_blueprint.route('/members/add_member', methods=['POST'])
def add_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    member_type = request.form['member_type']
    member_status = request.form['member_status']
    member = Member(first_name, last_name, member_type, member_status)
    member_repository.save(member)
    return redirect('/members')

@members_blueprint.route('/members/edit')
def edit():
    return render_template('members/edit.html', title='Edit Member')

@members_blueprint.route('/members/<id>/delete')
def delete_member(id):
    member = member_repository.view(id)
    return render_template('members/delete.html', title='Delete Member', member=member)

@members_blueprint.route('/members/<id>/delete_confirmation')
def delete_member_save(id):
    member_repository.delete_member(id)
    return redirect('/members')

