"""
Функции высшего порядка: Создайте функцию высшего порядка, которая принимает другую функцию и список чисел.
Функция высшего порядка должна возвращать список, содержащий результаты применения переданной функции
к каждому элементу списка.
"""


def higher_order_function(func, numbers):
    return [func(number) for number in numbers]


def square(x):
    return x * x


def cube(x):
    return x * x * x


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(higher_order_function(square, numbers))
    print(higher_order_function(cube, numbers))
