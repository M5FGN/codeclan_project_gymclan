from db.run_sql import run_sql

from models.member import Member
from models.gymsession import Gymsession
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gymsession_repository as gymsession_repository
import repositories.booking_repository as booking_repository

# For Set up - console.py

# Deleting all from Table
def delete_all():
    sql = 'DELETE FROM bookings'
    run_sql(sql)

def save(booking, member, gymsession):
    sql = 'INSERT INTO bookings (member_id, gymsession_id, attended) VALUES (%s, %s, %s) RETURNING id'
    values = [member.id, gymsession.id, booking.attended]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking


# Set Up? 

def view_all():
    bookings = []

    sql = 'SELECT * FROM bookings'
    results = run_sql(sql)

    for row in results:
        member = member_repository.view(row['member_id'])
        gymsession = gymsession_repository.view(row['gymsession_id'])
        booking = Booking(member, gymsession, row['attended'], row['id'])
        bookings.append(booking)
    return bookings

def member(booking):
    sql = 'SELECT * FROM members WHERE id = %s'
    values = [booking.member.id]
    results = run_sql(sql, values)[0]
    member = Member(results['first_name'], results['last_name'], results['member_type'], results['memeber_status'], results['id'])
    return member

def gymsession(booking):
    sql = 'SELECT * FROM gymsessions WHERE id = %s'
    values = [booking.gymsession.id]
    results = run_sql(sql, values)[0]
    gymsession = Gymsession(results['gs_title'], results['gs_description'], results['gs_type'], results['ability_level'], results['gs_day'], results['gs_date'], results['gs_time'], results['duration'], results['gs_plan'], results['gs_location'], results['cost'], results['capacity'], results['instructor'], results['id'])
    return gymsession
    


# Cancel Booking
def cancel_session(id):
    sql = 'DELETE FROM bookings WHERE id = %s'
    values = [id]
    run_sql(sql, values)



# Add Booking

def confirm_booking(member_id, gymsession_id):
   sql = 'INSERT INTO boookings (member_id, gymsession_id) VALUES (%s, %s)'
   values = [member.id, gymsession.id]
   run_sql(sql, values)


# Delete Participant
def delete(id):
    sql = 'DELETE FROM bookings WHERE id = %s'
    values = [id]
    run_sql(sql, values)


# New Save - Not touching the one above as its working - probably not correctly though.

def add_new(booking):
    sql = 'INSERT INTO bookings (member_id, gymsession_id) VALUES (%s, %s) RETURNING id'
    values = [booking.member.id, booking.gymsession.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    booking.id = id