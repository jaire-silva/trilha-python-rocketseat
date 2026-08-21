class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass


class Mamifero(Animal):
    def amamentar(self):
        print(f"{self.nome} está amamentando.")

class Ave(Animal):
    def voar(self):
        print(f"{self.nome} está voando.")

class Morcego(Mamifero, Ave):
    def emitir_som(self):
        super().emitir_som()
        print(f"Morcegos emitem sons ultrassônicos.")

morcego = Morcego("Batman")
morcego.emitir_som()
morcego.amamentar()
morcego.voar()