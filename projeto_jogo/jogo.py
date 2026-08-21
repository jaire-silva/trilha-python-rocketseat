from personagem import Personagem as _Personagem
from heroi import Heroi as _Heroi
from inimigo import Inimigo as _Inimigo

personagem = _Heroi("Herói", 200, 2, "Bola de Fogo")
print(personagem.exibir_detalhes())

print()

inimigo = _Inimigo("Morcego", 50, 3, "Voador")
print(inimigo.exibir_detalhes())