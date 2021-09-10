"""
    - Criando minha versao de loop
"""


def mine_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


