from flask import Flask, render_template
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def members():
    return render_template('members/index.html', title='Members')