import unittest

from models.member import Member
from models.session import Session
from models.booking import Booking

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.member1 = Member('Diana', 'Prince', 'Premium', 'Active', 1)
        self.member2 = Member('Bruce', 'Wayne', 'Premium', 'Inactive', 2)
        self.member3 = Member('Peter', 'Parker', 'Standard', 'Active', 3)

        self.session1 = Session('Les Mills - Body Pump', 'A full body weights workout.', 'Strength', 'Moderate', 'Monday', '05/04/21', '13.00', 45, 'Peak', 'Gym 1', 4.50, 10, 'Lonnie Machin', 1)
        self.session2 = Session('Les Mills - Body Combat', 'High energy martial arts inspired workout.', 'Cardio', 'Advanced', 'Wednesday', '07/04/21', '15.00', 60, 'Off Peak', 'Gym 2', 4.50, 10, 'Selina Kyle', 2)
        self.session3 = Session('Les Mills - Body Balance', 'A Yoga based class that will improve your mind, your body and your life', 'Flexibility', 'Beginner', 'Friday', '09/04/21', '11.00', 90, 'Peak', 'Gym 2', 4.50, 15, 'Selina Kyle', 3)

        
        self.booking1 = Booking(self.member1.member_id, self.session3.session_id)
        self.booking2 = Booking(self.member2.member_id, self.session1.session_id, True, 2)
        self.booking3 = Booking(self.member2.member_id, self.session3.session_id, True, 3)


    def test_booking_has__booking_id(self):
        self.assertEqual(None, self.booking1.booking_id)
        self.assertEqual(2, self.booking2.booking_id)
        self.assertEqual(3, self.booking3.booking_id)
    
    def test_booking_has__member_id(self):
        self.assertEqual(1, self.booking1.member_id)
        self.assertEqual(2, self.booking2.member_id)
        self.assertEqual(2, self.booking3.member_id)

    def test_booking_has__session_id(self):
        self.assertEqual(3, self.booking1.session_id)
        self.assertEqual(1, self.booking2.session_id)
        self.assertEqual(3, self.booking3.session_id)

    def test_booking_has__attended(self):
        self.assertEqual(False, self.booking1.attended)
        self.assertEqual(True, self.booking2.attended)
        self.assertEqual(True, self.booking3.attended)