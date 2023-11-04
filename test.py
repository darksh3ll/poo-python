<<<<<<< HEAD
import uuid
class Bank:
    def __init__(self,nom,solde=0):
        self.nom = nom
        self.solde = solde

=======
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
>>>>>>> main

class Client:
    def __init__(self,nom,prenom,banque):
        self.id = str(uuid.uuid4())[:8]
        self.nom = nom
        self.prenom = prenom
        self.banque = banque

<<<<<<< HEAD
    def depose_argent(self,depot):
        pass

# client1
bank1 = Bank("caisse d'epargne")
client1 = Client("Doe", "John", bank1)

# client2
bank2 = Bank("cic")
client2 = Client("stephane", "job", bank2)

client2.depose_argent(100)
print(client2.banque.solde)
=======

class Car(Vehicule):
    def __init__(self, marque, genre, color, chevaux):
        super().__init__(marque, genre, color)
        self.chevaux = chevaux


class Moto(Vehicule):
    def __init__(self, marque, genre, color):
        super().__init__(marque, genre, color)


a = Car("porshe", "voiture", "rouge", 110)
a.afficher_a()
>>>>>>> main
