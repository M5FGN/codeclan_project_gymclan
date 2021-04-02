class Session:

    def __init__(self, session_id, session_title, session_description, ability_level, session_date, session_time, duration, location, cost, capacity, instructor):
        self.session_id = session_id
        self.session_title = session_title
        self.session_description = session_description
        self.ability_level = ability_level
        self.session_date = session_date
        self.session_time = session_time
        self.duration = duration
        self.location = location
        self.cost = cost
        self.capacity = capacity
        self.instructor = instructor
        