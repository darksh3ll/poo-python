class Bird:
    def fly(self):
        print("je vole")


class Parrot:
    def __init__(self) :
        self.wing = Bird()


a = Parrot()
a.wing.fly()