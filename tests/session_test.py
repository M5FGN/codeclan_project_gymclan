import unittest

from models.session import Session

class TestSession(unittest.TestCase):

    def setUp(self):
        self.session1 = Session(1, 'Les Mills - Body Pump', 'A full body weights workout.', 'Strength', 'Moderate', 'Monday', '05/04/21', '13.00', 45, 'Peak', 'Gym 1', 4.50, 10, 'Lonnie Machin')
        self.session2 = Session(2, 'Les Mills - Body Combat', 'High energy martial arts inspired workout.', 'Cardio', 'Advanced', 'Wednesday', '07/04/21', '15.00', 60, 'Off Peak', 'Gym 2', 4.50, 10, 'Selina Kyle')
        self.session3 = Session(3, 'Les Mills - Body Balance', 'A Yoga based class that will improve your mind, your body and your life', 'Flexibility', 'Beginner', 'Friday', '09/04/21', '11.00', 90, 'Peak', 'Gym 2', 4.50, 15, 'Selina Kyle')

    def test_session_has__session_id(self):
        self.assertEqual(1, self.session1.session_id)
        self.assertEqual(2, self.session2.session_id)
        self.assertEqual(3, self.session3.session_id)
    
    def test_session_has__session_title(self):
        self.assertEqual('Les Mills - Body Pump', self.session1.session_title)
        self.assertEqual('Les Mills - Body Combat', self.session2.session_title)
        self.assertEqual('Les Mills - Body Balance', self.session3.session_title)

    def test_session_has__session_description (self):
        self.assertEqual('A full body weights workout.', self.session1.session_description)
        self.assertEqual('High energy martial arts inspired workout.', self.session2.session_description)
        self.assertEqual('A Yoga based class that will improve your mind, your body and your life', self.session3.session_description)

    def test_session_has__session_type(self):
        self.assertEqual('Strength', self.session1.session_type)
        self.assertEqual('Cardio', self.session2.session_type)
        self.assertEqual('Flexibility', self.session3.session_type)

    def test_session_has__ability_level(self):
        self.assertEqual('Moderate', self.session1.ability_level)
        self.assertEqual('Advanced', self.session2.ability_level)
        self.assertEqual('Beginner', self.session3.ability_level)
    
    def test_session_has__session_day(self):
        self.assertEqual('Monday', self.session1.session_day)
        self.assertEqual('Wednesday', self.session2.session_day)
        self.assertEqual('Friday', self.session3.session_day)
    
    def test_session_has__session_date (self):
        self.assertEqual('05/04/21', self.session1.session_date)
        self.assertEqual('07/04/21', self.session2.session_date)
        self.assertEqual('09/04/21', self.session3.session_date)
    
    def test_session_has__session_time(self):
        self.assertEqual('13.00', self.session1.session_time)
        self.assertEqual('15.00', self.session2.session_time)
        self.assertEqual('11.00', self.session3.session_time)
    
    def test_session_has__duration(self):
        self.assertEqual(45, self.session1.duration)
        self.assertEqual(60, self.session2.duration)
        self.assertEqual(90, self.session3.duration)

    def test_session_has__plan(self):
        self.assertEqual('Peak', self.session1.plan)
        self.assertEqual('Off Peak', self.session2.plan)
        self.assertEqual('Peak', self.session3.plan)

    def test_session_has__location(self): 
        self.assertEqual('Gym 1', self.session1.location)
        self.assertEqual('Gym 2', self.session2.location)
        self.assertEqual('Gym 2', self.session3.location)
    
    def test_session_has__cost(self):
        self.assertEqual(4.50, self.session1.cost)
        self.assertEqual(4.50, self.session2.cost)
        self.assertEqual(4.50, self.session3.cost)
    
    def test_session_has__capacity(self):
        self.assertEqual(10, self.session1.capacity)
        self.assertEqual(10, self.session2.capacity)
        self.assertEqual(15, self.session3.capacity)
    
    def test_session_has__instructor(self):
        self.assertEqual('Lonnie Machin', self.session1.instructor)
        self.assertEqual('Selina Kyle', self.session2.instructor)
        self.assertEqual('Selina Kyle', self.session3.instructor)
    
    