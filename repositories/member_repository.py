from db.run_sql import run_sql

from models.member import Member
from models.gymsession import Gymsession
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gymsession_repository as gymsession_repository
import repositories.booking_repository as booking_repository

def delete_all():
    sql = 'DELETE FROM members'
    run_sql(sql)

def save(member):
    sql = 'INSERT INTO members(first_name, last_name, member_type, member_status) VALUES (%s, %s, %s, %s) RETURNING id'
    values = [member.first_name, member.last_name, member.member_type, member.member_status]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def view_all():
    members=[]

    sql = 'SELECT * FROM members'
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['member_type'], row['member_status'], row['id'])
        members.append(member)
    return members

def view(id):
    member = None
    sql = 'SELECT * FROM members WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['member_type'], result['member_status'], result['id'])
    return member