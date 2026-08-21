from personagem import Personagem as _Personagem


class Inimigo(_Personagem):

    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \nTipo: {self.get_tipo()}"
