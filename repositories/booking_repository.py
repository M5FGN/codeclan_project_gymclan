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
