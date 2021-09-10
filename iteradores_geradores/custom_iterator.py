"""
    - Escrevendo um iterador customizado!
"""


class Counter:
    def __init__(self, smaller, bigger):
        self.smaller = smaller
        self.bigger = bigger

    def __str__(self):
        return f'smaller: {self.smaller}  bigger: {self.bigger}'

    def __int__(self):
        return self

    def __next__(self):
        if self.smaller < self.bigger:
            number = self.smaller
            self.smaller += 1
            return number
        raise StopIteration

