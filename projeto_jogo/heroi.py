import random

from personagem import Personagem as _Personagem

__all__ = ['Heroi']


class Heroi(_Personagem):

    def __init__(self, nome: str, vida: int, nivel: int, habilidade: str):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \nHabilidade: {self.get_habilidade()}"

    def ataque_especial(self, alvo: _Personagem):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(
            f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!"
        )
