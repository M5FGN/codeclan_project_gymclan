class Gymsession:

    def __init__(self, title, description, type, ability_level, day, date, time, duration, plan, location, cost, capacity, instructor, gymsession_id = None):
        self.title = title
        self.description = description
        self.type = type
        self.ability_level = ability_level
        self.day = day
        self.date = date
        self.time = time
        self.duration = duration
        self.plan = plan
        self.location = location
        self.cost = cost
        self.capacity = capacity
        self.instructor = instructor
        self.gymsession_id = gymsession_id
