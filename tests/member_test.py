import unittest

from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member1 = Member(1, 'Diana', 'Prince', 'Premium', 'Active')
        self.member2 = Member(2, 'Bruce', 'Wayne', 'Premium', 'Inactive')
        self.member3 = Member(3, 'Peter', 'Parker', 'Standard', 'Active')
    
    def test_member_has__member_id(self):
        self.assertEqual(1, self.member1.member_id)
        self.assertEqual(2, self.member2.member_id)
        self.assertEqual(3, self.member3.member_id)
    
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

    def test_member_has__status(self):
        self.assertEqual('Active', self.member1.status)
        self.assertEqual('Inactive', self.member2.status)
        self.assertEqual('Active', self.member3.status)

