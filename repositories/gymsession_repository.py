from db.run_sql import run_sql

from models.member import Member
from models.gymsession import Gymsession
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gymsession_repository as gymsession_repository
import repositories.booking_repository as booking_repository

def delete_all():
    sql = 'DELETE FROM gymsessions'
    run_sql(sql)

def save(gymsession):
    sql = 'INSERT INTO gymsessions(gs_title, gs_description, gs_type, ability_level, gs_day, gs_date, gs_time, duration, gs_plan, gs_location, cost, capacity, instructor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id'
    values = [gymsession.gs_title, gymsession.gs_description, gymsession.gs_type, gymsession.ability_level, gymsession.gs_day, gymsession.gs_date, gymsession.gs_time, gymsession.duration, gymsession.gs_plan, gymsession.gs_location, gymsession.cost, gymsession.capacity, gymsession.instructor]
    results = run_sql(sql, values)
    gymsession.id = results[0]['id']
    return gymsession

def view_all():
    gymsessions=[]

    sql = 'SELECT * FROM gymsessions'
    results = run_sql(sql)
    for row in results:
        gymsession = Gymsession(row['gs_title'], row['gs_description'], row['gs_type'], row['ability_level'], row['gs_day'], row['gs_date'], row['gs_time'], row['duration'], row['gs_plan'], row['gs_location'], row['cost'], row['capacity'], row['instructor'], row['id'])
        gymsessions.append(gymsession)
    return gymsessions

def view(id):
    gymsession = None
    sql = 'SELECT * FROM gymsessions WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gymsession = Gymsession(result['gs_title'], result['gs_description'], result['gs_type'], result['ability_level'], result['gs_day'], result['gs_date'], result['gs_time'], result['duration'], result['gs_plan'], result['gs_location'], result['cost'], result['capacity'], result['instructor'], result['id'])
    return gymsession


def delete_gymsession(id):
    sql = 'DELETE FROM gymsessions WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def participants(gymsession):
    members = []
    sql = 'SELECT * FROM bookings INNER JOIN members ON members.id = bookings.member_id WHERE gymsession_id = %s'
    values = [gymsession.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['member_type'], row['member_status'], row['id'])
        members.append(member)
    return members



def edit_gymsession(gymsession):
    sql = 'UPDATE gymsessions SET (gs_title, gs_description, gs_type, ability_level, gs_day, gs_date, gs_time, duration, gs_plan, gs_location, cost, capacity, instructor) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s'
    values = [gymsession.gs_title, gymsession.gs_description, gymsession.gs_type, gymsession.ability_level, gymsession.gs_day, gymsession.gs_date, gymsession.gs_time, gymsession.duration, gymsession.gs_plan, gymsession.gs_location, gymsession.cost, gymsession.capacity, gymsession.instructor, gymsession.id]
    run_sql(sql, values)


def bookings(gymsession):
    sql = 'SELECT * FROM bookings WHERE gymsession_id = %s'
    values = [gymsession.id]
    results = run_sql(sql, values)
    bookings = []
    for row in results:
        member = member_repository.view(row['member_id'])
        gymsession = gymsession_repository.view(row['gymsession_id'])
        booking = Booking(member, gymsession, row['attended'], row['id'])
        bookings.append(booking)
    return bookings
