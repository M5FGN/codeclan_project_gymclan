class Booking:

    def __init__(self, member_id, session_id, attended = False, booking_id = None):
        self.member_id = member_id
        self.session_id = session_id
        self.attended = attended
        self.booking_id = booking_id

    def add_attendance(self):
        self.attended = True

