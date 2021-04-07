class Booking:

    def __init__(self, member, gymsession, attended = False, id = None):
        self.member = member
        self.gymsession = gymsession
        self.attended = attended
        self.id = id

    def add_attendance(self):
        self.attended = True

