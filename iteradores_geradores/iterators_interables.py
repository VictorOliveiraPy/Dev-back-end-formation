"""
Iterator ->
            - obj que pode ser iterado.
            - obj que retorna um dado, um elemento por vez, quando uma funcao next() e chamada;
            - StopIteration acontecer quando tentamos interar um valor que nao existe

Iterable ->
        - obj que ira retornar um iterator quando a funcao iter() for chamada.
"""

name = 'victor'


for n in name:
    print(n)