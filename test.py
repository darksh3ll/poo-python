import uuid
class Bank:
    def __init__(self,nom,solde=0):
        self.nom = nom
        self.solde = solde


class Client:
    def __init__(self,nom,prenom,banque):
        self.id = str(uuid.uuid4())[:8]
        self.nom = nom
        self.prenom = prenom
        self.banque = banque

    def depose_argent(self,depot):
        pass

# client1
bank1 = Bank("caisse d'epargne")
client1 = Client("Doe", "John", bank1)

# client2
bank2 = Bank("cic")
client2 = Client("stephane", "bob", bank2)

client2.depose_argent(100)
print(client2.banque.solde)
