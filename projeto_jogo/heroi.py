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
