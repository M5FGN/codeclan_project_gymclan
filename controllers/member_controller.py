from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.member import Member
from models.gymsession import Gymsession
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gymsession_repository as gymsession_repository
import repositories.booking_repository as booking_repository

members_blueprint = Blueprint('members', __name__)

# View Members

@members_blueprint.route('/members')
def members():
    members = member_repository.view_all()
    return render_template('members/index.html', title='Members', members=members)

@members_blueprint.route('/members/<id>')
def view(id):
    member = member_repository.view(id)
    return render_template('members/member.html', title='Member Profile', member=member)  
# TODO Add title Members Name


# Add Members

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

# Delete Members

@members_blueprint.route('/members/<id>/delete')
def delete_member(id):
    member = member_repository.view(id)
    return render_template('members/delete.html', title='Delete Member', member=member)

@members_blueprint.route('/members/<id>/delete_confirmation')
def delete_member_save(id):
    member_repository.delete_member(id)
    return redirect('/members')

# Edit Members

@members_blueprint.route('/members/<id>/edit', methods=['GET'])
def edit(id):
    member = member_repository.view(id)
    return render_template('members/edit.html', title='Edit Member', member=member)

@members_blueprint.route('/members/<id>/edit_save', methods=['POST'])
def edit_save(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    member_type = request.form['member_type']
    member_status = request.form['member_status']
    member = Member(first_name, last_name, member_type, member_status, id)
    member_repository.edit_member(member)
    return redirect('/members')

# View Session History

@members_blueprint.route('/members/<id>/history')
def history(id):
    member = member_repository.view(id)
    gymsessions = member_repository.history(member)
    return render_template ('members/history.html', title='Session History', member=member, gymsessions=gymsessions)


# FIXME
# Filters 

# @members_blueprint.route('/members/filter', methods=['POST'])
# def filter():
#     filter_member_status = request.form['status_filter']
#     # members = member_repository.filter(filter_member_status)
#     return redirect('/members/index.html')





