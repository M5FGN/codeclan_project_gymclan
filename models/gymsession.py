class Gymsession:

    def __init__(self, gs_title, gs_description, gs_type, ability_level, gs_day, gs_date, gs_time, duration, gs_plan, gs_location, cost, capacity, instructor, id = None):
        self.gs_title = gs_title
        self.gs_description = gs_description
        self.gs_type = gs_type
        self.ability_level = ability_level
        self.gs_day = gs_day
        self.gs_date = gs_date
        self.gs_time = gs_time
        self.duration = duration
        self.gs_plan = gs_plan
        self.gs_location = gs_location
        self.cost = cost
        self.capacity = capacity
        self.instructor = instructor
        self.id = id
