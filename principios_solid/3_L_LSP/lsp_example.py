class Animal:
    def comer(self):
        print("O Animal está comendo.")

    def andar(self):
        print("O Animal está andando na jaula.")


class Felino(Animal):
    def lamber(self):
        print("O Felino está lambendo seu pelo.")

    def comer(self):
        print("O Felino come sua ração.")


class Leao(Felino):
    def rugir(self):
        print("O Leão está rugindo alto.")


class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()


animal = Animal()
felino = Felino()

animal.comer()
felino.comer()