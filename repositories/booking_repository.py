from db.run_sql import run_sql

from models.member import Member
from models.gymsession import Gymsession
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gymsession_repository as gymsession_repository
import repositories.booking_repository as booking_repository

def delete_all():
    sql = 'DELETE FROM bookings'
    run_sql(sql)

def save(booking, member, gymsession):
    sql = 'INSERT INTO bookings (member_id, gymsession_id, attendance) VALUES (%s, %s, %s) RETURNING id'
    values = [member.id, gymsession.id, booking.attended]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking