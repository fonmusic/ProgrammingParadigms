"""
Логическое программирование
Задача 2: Напишите программу, которая сортирует список чисел методом сортировки слиянием.
Сортировка слиянием - это эффективный алгоритм сортировки, который разбивает список на две половины,
сортирует их отдельно, а затем объединяет в отсортированный список. Задача состоит в том, чтобы написать
программу, которая будет сортировать список чисел методом сортировки слиянием.

Пример решения:
Программа принимает на вход список чисел, который нужно отсортировать.
Если список состоит из одного элемента или пуст, он считается уже отсортированным.
В противном случае список разделяется на две половины.
Рекурсивно вызывается сортировка слиянием для каждой половины.
Затем отсортированные половины сливаются в один отсортированный список.
Конечный отсортированный список возвращается.
"""


def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


if __name__ == '__main__':
    print('Введите список чисел через пробел:')
    array = [int(i) for i in input().split()]
    print(*merge_sort(array))
