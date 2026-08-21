# Exemplo de classe
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Idade: {self.idade}"

    def saudacao(self) -> str:
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


# Exemplo de objeto
pessoa1 = Pessoa("Alice", 30)
print(pessoa1.saudacao())

pessoa2 = Pessoa("Rodrigo", 32)
print(pessoa2.saudacao())