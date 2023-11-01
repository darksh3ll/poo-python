import random

class Vehicule:
    def __init__(self,marque,genre,color):
        self.marque =marque
        self.genre = genre
        self.color = color

class Car(Vehicule):
    def __init__(self, marque, genre,color,chevaux):
        super().__init__(marque, genre,color)
        self.chevaux=chevaux


class Moto(Vehicule):
    def __init__(self, marque, genre, color):
        super().__init__(marque, genre, color)


a = Car("porshe","voiture","rouge",110)
b = Moto("ducati",'moto',"bleu",150)
print(b.color)