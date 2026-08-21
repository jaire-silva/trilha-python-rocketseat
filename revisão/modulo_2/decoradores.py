# Decoradores
def meu_decorator(funcao):
    def wrapper():
        print('Antes da minha função ser chamada')
        funcao()
        print('Depois da minha função ser chamada')
    return wrapper


@meu_decorator
def minha_funcao():
    print("Minha função foi chamada")


minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self, funcao):
        self.funcao = funcao

    def __call__(self):
        print("Antes da função ser chamada (decorador de classe)")
        self.funcao
        print('Depois da minha função ser chamada  (decorador de classe)')


@MeuDecoradorDeClasse
def segundaFuncao():
    print("Segunda função foi chamada")

segundaFuncao()