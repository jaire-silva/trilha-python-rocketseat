"""
exc_type: O tipo de exceção que ocorreu, se houver. Se não ocorreu nenhuma, este
    parâmetro será Nome.

exc_value: O valor da exceção que ocorreu, se houver. Se não ocorreu nenhuma, este
    parâmetro será Nome.

exc_tb: O traceback (rastreamento de pilha) associado à exceção que ocorreu. Se não ocorreu nenhuma, este
    parâmetro será Nome.
"""


class AlgumaCoisa:
    def __enter__(self):
        print('Estou entrando')

    def __exit__(self, exc_type, exc_value, traceback):
        print('Estou saindo')


with AlgumaCoisa() as something:
    print("Estou no meio")
