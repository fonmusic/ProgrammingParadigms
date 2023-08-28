"""
Ленивые вычисления: Напишите функцию, которая будет генерировать бесконечную последовательность простых чисел.
Используйте ленивые вычисления, чтобы генерировать только те числа, которые действительно нужны.
"""


def prime_numbers():
    n = 2
    while True:
        if all(n % i != 0 for i in range(2, n)):
            yield n
        n += 1


if __name__ == '__main__':
    prime = prime_numbers()
    for i in range(11):
        print(next(prime))
