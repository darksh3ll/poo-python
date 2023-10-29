import random

class Joueur:
    def __init__(self,nom,score=0):
        self.nom = nom
        self.score = score


class Game:
    def __init__(self,joueur1,joueur2):
        pass


    @staticmethod
    def lance_de():
         return random.randint(1, 6)
        


joueur1 = Joueur("stephane")
joueur2 = Joueur("Joel")

