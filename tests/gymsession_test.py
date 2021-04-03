import unittest

from models.gymsession import Gymsession

class TestGymsession(unittest.TestCase):

    def setUp(self):
        self.gymsession1 = Gymsession('Les Mills - Body Pump', 'A full body weights workout.', 'Strength', 'Moderate', 'Monday', '05/04/21', '13.00', 45, 'Peak', 'Gym 1', 4.50, 10, 'Lonnie Machin')
        self.gymsession2 = Gymsession('Les Mills - Body Combat', 'High energy martial arts inspired workout.', 'Cardio', 'Advanced', 'Wednesday', '07/04/21', '15.00', 60, 'Off Peak', 'Gym 2', 4.50, 10, 'Selina Kyle', 2)
        self.gymsession3 = Gymsession('Les Mills - Body Balance', 'A Yoga based class that will improve your mind, your body and your life', 'Flexibility', 'Beginner', 'Friday', '09/04/21', '11.00', 90, 'Peak', 'Gym 2', 4.50, 15, 'Selina Kyle', 3)

    def test_gymsession_has__gymsession_id(self):
        self.assertEqual(None, self.gymsession1.id)
        self.assertEqual(2, self.gymsession2.id)
        self.assertEqual(3, self.gymsession3.id)
    
    def test_gymsession_has__title(self):
        self.assertEqual('Les Mills - Body Pump', self.gymsession1.gs_title)
        self.assertEqual('Les Mills - Body Combat', self.gymsession2.gs_title)
        self.assertEqual('Les Mills - Body Balance', self.gymsession3.gs_title)

    def test_gymsession_has__description(self):
        self.assertEqual('A full body weights workout.', self.gymsession1.gs_description)
        self.assertEqual('High energy martial arts inspired workout.', self.gymsession2.gs_description)
        self.assertEqual('A Yoga based class that will improve your mind, your body and your life', self.gymsession3.gs_description)

    def test_gymsession_has__type(self):
        self.assertEqual('Strength', self.gymsession1.gs_type)
        self.assertEqual('Cardio', self.gymsession2.gs_type)
        self.assertEqual('Flexibility', self.gymsession3.gs_type)

    def test_gymsession_has__ability_level(self):
        self.assertEqual('Moderate', self.gymsession1.ability_level)
        self.assertEqual('Advanced', self.gymsession2.ability_level)
        self.assertEqual('Beginner', self.gymsession3.ability_level)
    
    def test_gymsession_has__day(self):
        self.assertEqual('Monday', self.gymsession1.gs_day)
        self.assertEqual('Wednesday', self.gymsession2.gs_day)
        self.assertEqual('Friday', self.gymsession3.gs_day)
    
    def test_gymsession_has__date (self):
        self.assertEqual('05/04/21', self.gymsession1.gs_date)
        self.assertEqual('07/04/21', self.gymsession2.gs_date)
        self.assertEqual('09/04/21', self.gymsession3.gs_date)
    
    def test_gymsession_has__time(self):
        self.assertEqual('13.00', self.gymsession1.gs_time)
        self.assertEqual('15.00', self.gymsession2.gs_time)
        self.assertEqual('11.00', self.gymsession3.gs_time)
    
    def test_gymsession_has__duration(self):
        self.assertEqual(45, self.gymsession1.duration)
        self.assertEqual(60, self.gymsession2.duration)
        self.assertEqual(90, self.gymsession3.duration)

    def test_gymsession_has__plan(self):
        self.assertEqual('Peak', self.gymsession1.gs_plan)
        self.assertEqual('Off Peak', self.gymsession2.gs_plan)
        self.assertEqual('Peak', self.gymsession3.gs_plan)

    def test_gymsession_has__location(self): 
        self.assertEqual('Gym 1', self.gymsession1.gs_location)
        self.assertEqual('Gym 2', self.gymsession2.gs_location)
        self.assertEqual('Gym 2', self.gymsession3.gs_location)
    
    def test_gymsession_has__cost(self):
        self.assertEqual(4.50, self.gymsession1.cost)
        self.assertEqual(4.50, self.gymsession2.cost)
        self.assertEqual(4.50, self.gymsession3.cost)
    
    def test_gymsession_has__capacity(self):
        self.assertEqual(10, self.gymsession1.capacity)
        self.assertEqual(10, self.gymsession2.capacity)
        self.assertEqual(15, self.gymsession3.capacity)
    
    def test_gymsession_has__instructor(self):
        self.assertEqual('Lonnie Machin', self.gymsession1.instructor)
        self.assertEqual('Selina Kyle', self.gymsession2.instructor)
        self.assertEqual('Selina Kyle', self.gymsession3.instructor)
    
    