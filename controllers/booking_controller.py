from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.member import Member
from models.gymsession import Gymsession
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gymsession_repository as gymsession_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint('bookings', __name__)

# View Bookings - Route Not Used 

@bookings_blueprint.route('/bookings')
def view_all():
    bookings = booking_repository.view_all()
    return render_template('bookings/index.html', bookings=bookings)


# Memeber Cancel Booking

@bookings_blueprint.route('/bookings/<id>/cancel_session')
def cancel_session(booking):
    return render_template('bookings/cancel_session.html', Title='Cancel Session')


# Gymsession Delete Participant
@bookings_blueprint.route('/bookings/<id>/delete_participant')
def delete_participant(booking):
    bookings = booking_repository.delete_participant(id)
    return render_template('bookings/delete_participant.html', Title="Delete Participant")


# Add Booking

@bookings_blueprint.route('/bookings/<id>/add_session')
def book_session(id):
    member = member_repository.view(id)
    gymsessions = gymsession_repository.view_all()
    return render_template('bookings/book_session.html', title='Choose Session', member=member, gymsessions=gymsessions)

@bookings_blueprint.route('/bookings/<member_id>/<gymsession_id>/to_confirm')
def choose_session(member, gymsession):
    booking = booking_repository.confirm_booking(member.id, gymsession.id)
    return render_template('bookings/confirm_booking.html', title='Confirm Booking', member=member, gymsession=gymsession)