from datetime import datetime

class FitnessClass:
    def __init__(self, id, name, datetime_ist, instructor, slots):
        self.id = id
        self.name = name
        self.datetime_ist = datetime_ist
        self.instructor = instructor
        self.slots = slots
