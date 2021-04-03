class Booking:

    def __init__(self, member_id, gymsession_id, attended = False, id = None):
        self.member_id = member_id
        self.gymsession_id = gymsession_id
        self.attended = attended
        self.id = id

    def add_attendance(self):
        self.attended = True

