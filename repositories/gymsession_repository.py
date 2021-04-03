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