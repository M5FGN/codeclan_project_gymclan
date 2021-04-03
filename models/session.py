class Session:

    def __init__(self, session_id, session_title, session_description, session_type, ability_level, session_day, session_date, session_time, duration, plan, location, cost, capacity, instructor):
        self.session_id = session_id
        self.session_title = session_title
        self.session_description = session_description
        self.session_type = session_type
        self.ability_level = ability_level
        self.session_day = session_day
        self.session_date = session_date
        self.session_time = session_time
        self.duration = duration
        self.plan = plan
        self.location = location
        self.cost = cost
        self.capacity = capacity
        self.instructor = instructor
