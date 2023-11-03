import random


class Vehicule:
    aba = [1,2,3,4,5]
    def __init__(self, marque, genre, color):
        self.marque = marque
        self.genre = genre
        self.color = color

    @classmethod
    def afficher_a(cls):
        for a in Vehicule.aba:
            print(a)



class Car(Vehicule):
    def __init__(self, marque, genre, color, chevaux):
        super().__init__(marque, genre, color)
        self.chevaux = chevaux


class Moto(Vehicule):
    def __init__(self, marque, genre, color):
        super().__init__(marque, genre, color)


a = Car("porshe", "voiture", "rouge", 110)
a.afficher_a()
