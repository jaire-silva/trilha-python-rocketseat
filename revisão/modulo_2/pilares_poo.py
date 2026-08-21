# Exemplo de herança

print("\nExemplo de Herança:")

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self, som):
        pass


class Cachorro(Animal):
    def emitir_som(self, *args, **kwargs):
        print(f"{self.__class__.__name__}: {'Au Au'}")

class Gato(Animal):
    def emitir_som(self, *args, **kwargs):
        print(f"{self.__class__.__name__}: {'Miau'}")

dog = Cachorro("Rex")
cat = Gato("Felix")

dog.emitir_som()
cat.emitir_som()

print("\nExemplo de Polimorfismo:")
animais = [dog, cat]

for animal in animais:
    animal.emitir_som()

print("\nExemplo de Encapsulamento:")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria(1000)

print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(500)
print(f"Saldo atualizada: {conta.consultar_saldo()}")
conta.depositar(-500)
print(f"Saldo atualizada: {conta.consultar_saldo()}")
conta.sacar(200)
print(f"Saldo atualizado: {conta.consultar_saldo()}")


print("\nExemplo de Abstração")
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class Carro(Veiculo):
    def ligar(self):
        print("Ligando o carro...")

    def desligar(self):
        print("Desligando o carro...")


class Moto(Veiculo):
    def ligar(self):
        print("Ligando a moto...")

    def desligar(self):
        print("Desligando a moto...")


carro_amarelo = Carro()
carro_amarelo.ligar()
carro_amarelo.desligar()