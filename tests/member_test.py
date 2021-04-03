import unittest

from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member1 = Member('Diana', 'Prince', 'Premium', 'Active')
        self.member2 = Member('Bruce', 'Wayne', 'Premium', 'Inactive', 2)
        self.member3 = Member('Peter', 'Parker', 'Standard', 'Active', 3)
    
    def test_member_has__id(self):
        self.assertEqual(None, self.member1.id)
        self.assertEqual(2, self.member2.id)
        self.assertEqual(3, self.member3.id)
    
    def test_member_has__first_name(self):
        self.assertEqual('Diana', self.member1.first_name)
        self.assertEqual('Bruce', self.member2.first_name)
        self.assertEqual('Peter', self.member3.first_name)

    def test_member_has__last_name(self):
        self.assertEqual('Prince', self.member1.last_name)
        self.assertEqual('Wayne', self.member2.last_name)
        self.assertEqual('Parker', self.member3.last_name)
    
    def test_member_has__member_type(self):
        self.assertEqual('Premium', self.member1.member_type)
        self.assertEqual('Premium', self.member2.member_type)
        self.assertEqual('Standard', self.member3.member_type)

    def test_member_has__member_status(self):
        self.assertEqual('Active', self.member1.member_status)
        self.assertEqual('Inactive', self.member2.member_status)
        self.assertEqual('Active', self.member3.member_status)

