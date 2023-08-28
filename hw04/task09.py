"""
Чистые функции и неизменяемость данных: Напишите функцию, которая принимает список чисел
и возвращает новый список, в котором каждый элемент умножен на 2.
Убедитесь, что вы используете только чистые функции и не изменяете исходный список.
"""


def double_list(numbers):
    return [number * 2 for number in numbers]


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(f'Original list: {numbers}')
    print(f'Doubled list: {double_list(numbers)}')
    print(f'Original list: {numbers}')