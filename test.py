
class Animal:
    """class animal
    """

    def __init__(self,nom):
        self.nom = nom

    def se_presenter(self):
        print(f"Je suis un animal et je m'appelle {self.nom}.")


class Oiseau(Animal):
    def __init__(self, nom,peut_voler):
        super().__init__(nom)
        self.peut_voler = peut_voler
    
    def se_presenter(self):
        super().se_presenter()
        if self.peut_voler:
            print("Je suis un oiseau et je peux voler !")
        else:
            print("Je suis un oiseau et je ne peux pas voler.")


# Création d'instances d'Oiseau
oiseau1 = Oiseau("Pépé", True)
oiseau2 = Oiseau("Kiwi", False)

# Appel de se_presenter pour chaque oiseau
oiseau1.se_presenter()
oiseau2.se_presenter()
organismes.stephane@proton.me

