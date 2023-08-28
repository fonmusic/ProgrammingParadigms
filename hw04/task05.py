"""
Функции-редуцеры для списков: Напишите функцию-редуктор, которая принимает список строк
и возвращает строку, состоящую из объединенных элементов списка через запятую.
Например, для списка ["apple", "banana", "cherry"] результат должен быть "apple, banana, cherry".
"""


def join_strings(strings):
    return ', '.join(strings)


if __name__ == '__main__':
    print(join_strings(["apple", "banana", "cherry"]))
    