import unittest

from models.member import Member
from models.gymsession import Gymsession
from models.booking import Booking


class TestBooking(unittest.TestCase):

    def setUp(self):
        self.member1 = Member('Diana', 'Prince', 'Premium', 'Active', 1)
        self.member2 = Member('Bruce', 'Wayne', 'Premium', 'Inactive', 2)
        self.member3 = Member('Peter', 'Parker', 'Standard', 'Active', 3)

        self.gymsession1 = Gymsession('Les Mills - Body Pump', 'A full body weights workout.', 'Strength', 'Moderate', 'Monday', '05/04/21', '13.00', 45, 'Peak', 'Gym 1', 4.50, 10, 'Lonnie Machin')
        self.gymsession2 = Gymsession('Les Mills - Body Combat', 'High energy martial arts inspired workout.', 'Cardio', 'Advanced', 'Wednesday', '07/04/21', '15.00', 60, 'Off Peak', 'Gym 2', 4.50, 10, 'Selina Kyle', 2)
        self.gymsession3 = Gymsession('Les Mills - Body Balance', 'A Yoga based class that will improve your mind, your body and your life', 'Flexibility', 'Beginner', 'Friday', '09/04/21', '11.00', 90, 'Peak', 'Gym 2', 4.50, 15, 'Selina Kyle', 3)

        self.booking1 = Booking(self.member1.id, self.gymsession3.id)
        self.booking2 = Booking(self.member2.id, self.gymsession1.id, True, 2)
        self.booking3 = Booking(self.member2.id, self.gymsession3.id, True, 3)

    def test_booking_has__booking_id(self):
        self.assertEqual(None, self.booking1.id)
        self.assertEqual(2, self.booking2.id)
        self.assertEqual(3, self.booking3.id)
    
    def test_booking_has__member_id(self):
        self.assertEqual(1, self.booking1.member_id)
        self.assertEqual(2, self.booking2.member_id)
        self.assertEqual(2, self.booking3.member_id)

    def test_booking_has__gymsession_id(self):
        self.assertEqual(3, self.booking1.gymsession_id)
        self.assertEqual(None, self.booking2.gymsession_id)
        self.assertEqual(3, self.booking3.gymsession_id)

    def test_booking_has__attendance(self):
        self.assertEqual(False, self.booking1.attended)
        self.assertEqual(True, self.booking2.attended)
        self.assertEqual(True, self.booking3.attended)

    def test_mark_class_as_attended(self):
        self.booking1.add_attendance()
        self.assertEqual(True, self.booking1.attended)

