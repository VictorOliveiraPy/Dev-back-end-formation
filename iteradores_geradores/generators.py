"""
    - Generators sao iterators (Iteradores);
    - Obs: O contrario nao e verdadeiro. nem todo iterator e um generator
    Info
    - Generators podem ser criados com funcoes geradoras
    - funcoes geradoras utilizam a palavra reservada yield;
    - generators podem ser criados com expressoes geradoras;
--------------------------------------------------------------------------------
    Funcoes                                      | Generator Functions
    utilizam return                              | utilizam yield
    retorna uma vez                              | podem utilizar yield multiplas vezes
    quando executada, retornar um valor or none  | quando executada, retornar um generator
"""


# Generators Function

# Gera um generator


def count_until(value_maximum):
    counter = 1
    while counter <= value_maximum:
        yield counter
        counter += 1


count = count_until(6)

for c in count:
    print(next(count))
