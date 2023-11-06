class Etudiant:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
        matiere = {}


class Matiere:
    matieres = ["math","Francais","musique"]
    def __init__(self,nom):
        self.nom = nom

    @classmethod
    def initialiser_matieres(cls):
         for nom in cls.matieres:
            setattr(cls, nom, Matiere(nom))
      


Matiere.initialiser_matieres()

print(Matiere.math.nom)  