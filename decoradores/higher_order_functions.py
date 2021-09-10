"""
 - Podemos ter funcoes que retornam outras funcoes como resultado
 - ou ate mesmo podemos passar funcoes como argumentos para outras funcoes,
 - e ate mesmo criar variaveis do tipo funcoes

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


print(calculate(4, 3, multiply))