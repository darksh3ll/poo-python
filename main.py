import uuid
from datetime import datetime

class parking:
    def __init__(self,place):
        self.place = place



class Car:
    def __init__(self):
        self.ticket_number = uuid.uuid4()
        self.entry_hours = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def __str__(self):
        return f"Car ID: {self.ticket_number} Entry Hours :{self.entry_hours}"


a = Car()
b= Car()
print(a)
print(b)