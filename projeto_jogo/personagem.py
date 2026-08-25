import random
from abc import ABC as _ABC


class Personagem(_ABC):
    def __init__(self, nome: str, vida: int, nivel: int):
        if type(self) is Personagem:
            raise TypeError("A classe 'Personagem' é abstrata e não pode ser instanciada diretamente.")

        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def receber_ataque(self, dano):
        self.__vida -= dano

        if self.__vida <= 0:
            self.__vida = 0
            print(f"{self.get_nome()} morreu!")

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
        alvo.receber_ataque(dano)

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} \nVida: {self.get_vida()} \nNível: {self.get_nivel()}"
