# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10

    def __init__(self, nome):
        self.nome = nome

    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"

    @classmethod
    def metodo_classe(cls):
        return f"Método de classe chamado com valor {cls.valor}"

    @staticmethod
    def metodo_estatico():
        return f"Método estático chamado com valor {MinhaClasse.valor}"


obj = MinhaClasse("Classe de exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, ano)

    @staticmethod
    def print_carro(carro):
        print(f"Marca: {carro.marca}, Modelo: {carro.modelo}, Ano: {carro.ano}")


configuracao = "Toyota,Corolla,2022"

carro = Carro.criar_carro(configuracao)
Carro.print_carro(carro)

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b

print(Matematica.somar(5, 3))