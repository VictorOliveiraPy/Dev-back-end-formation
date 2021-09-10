"""
 - Podemos ter funcoes que retornam outras funcoes como resultado
 - ou ate mesmo podemos passar funcoes como argumentos para outras funcoes,
 - e ate mesmo criar variaveis do tipo funcoes

 First Class Citizen

"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def share(a, b):
    return a / b


def calculate(num1, num2, fuction):
    return fuction(num1, num2)


# Nested Functions - Funcoes aninhadas


#   Funcoes dentro de funcoes, conhecida por Nested Functions or Innter Functions (Funcoes Internas)


from random import choice


def greeting(people):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de voce '))

    return humor() + people


# return function  of others function

def make_me_laugh():
    def to_laugh():
        return choice(('ahahahahahaha', 'asahsuahsuahsa', 'uauauauaush'))

    return to_laugh()


# Inner Functions (Funcoes Internas / Nested Functions) Podem acessar o escopo de funcoes mais externas.

def make_me_laugh_again(people):
    def laughing():
        r = choice(('ahsauhuahusa', 'hahaahahah', 'k'))
        return f'{r} {people}'

    return laughing()


people = make_me_laugh_again('victor')
print(people)
