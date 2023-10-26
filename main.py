import uuid
from datetime import datetime

class parking:
    place = 2

    def __str__(self) -> str:
        return f"Le parking contient {self.place} places"

    @classmethod
    def park_car(cls):
        """reduit le nombre de place"""
        if cls.place > 0:
            cls.place -= 1
        else:
            print("Le parking est plein")



class Car:
    def __init__(self):
        self.ticket_number = uuid.uuid4()
        self.entry_hours = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def __str__(self):
        return f"Car ID: {self.ticket_number} Entry Hours :{self.entry_hours}"
    
    def enter_parking(self):
        parking.park_car()

    

p = parking()
car1 =Car()
car2 =Car()
car3 =Car()

car1.enter_parking()
car2.enter_parking()
car3.enter_parking()
print(p.place)
