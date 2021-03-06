from functools import cache, lru_cache

"""
# cachea todos os valores @cache
lru_cache(maxsize=value) faz cache de uma quantidade especificar de valores
"""


@lru_cache(maxsize=5)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    for i in range(400):
        print(i, fib(i))
    print("done")


if __name__ == '__main__':
    main()
