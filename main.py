import uuid
from datetime import datetime


class parking:
    place = 6
    car_in_parking = []

    def __str__(self) -> str:
        return f"Le parking contient {self.place} places"

    @classmethod
    def park_car(cls,car):
        """reduit le nombre de place"""
        if cls.place > 0:
            cls.place -= 1
            cls.car_in_parking.append(car)
        else:
            print("Le parking est plein")

    def nbr_car(cls):






    @classmethod
    def remove_car_by_uuid(cls, car_uuid):
    # Trouver la voiture avec l'UUID correspondant
        for index, car in enumerate(cls.car_in_parking):
            if car.ticket_number == car_uuid:
                # Retirer la voiture du parking
                cls.car_in_parking.pop(index)
                 # Augmenter le nombre de places
                cls.place += 1
                print(f"La voiture {car_uuid} a quitté le parking.")
                return
            print("Aucune voiture avec cet UUID trouvé dans le parking.")

         
    @classmethod
    def place_dispo(cls):
        print(cls.place - len(cls.car_in_parking))
      
            
class Car:
    def __init__(self):
        self.ticket_number = str(uuid.uuid4())[:8]
        self.entry_hours = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def __str__(self):
        return f"Car ID: {self.ticket_number} Entry Hours :{self.entry_hours}"
    
    def enter_parking(self):
        parking.park_car(self)

    

p = parking()

def main_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Entrer une voiture")
        print("2. Sortir une voiture ")
        print("3. Afficher le nombre de voitures dans le parking")
        print("4. Afficher le nombre de places disponibles")
        print("5. Quitter")
        choice = input("Sélectionnez une option : ")

        if choice == '1':
            car = Car()
            car.enter_parking()
        elif choice == '2':
            uuid = input("Entrez UUID: ")
            p.remove_car_by_uuid(uuid)
        elif choice == '3':
            p.nbr_car()
        elif choice == '4':
            p.place_dispo()
        elif choice == '5':
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main_menu()