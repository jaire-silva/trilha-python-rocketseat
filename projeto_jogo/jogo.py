from heroi import Heroi as _Heroi
from inimigo import Inimigo as _Inimigo


class Jogo:
    def __init__(self):
        self.heroi = _Heroi("Herói", 200, 2, "Bola de Fogo")
        self.inimigo = _Inimigo("Morcego", 50, 3, "Voador")

    def iniciar_batalha(self):
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print(f"\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhes())
            print()
            print(self.inimigo.exibir_detalhes())
            print()

            input("Pressione Enter para atacar...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida. Escolha novamente.")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("\nParabéns, você venceu a batalha!")
        else:
            print("\nVocê foi derrotado. Que pena!")
