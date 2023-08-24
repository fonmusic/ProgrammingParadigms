"""
Стратегия:
Реализуйте паттерн Стратегия на языке Python для сортировки списка чисел.
Создайте класс SortStrategy, имеющий метод sort(numbers), и несколько конкретных стратегий для различных методов сортировки
(например, пузырьковая сортировка, сортировка выбором).
"""


class SortStrategy:
    def sort(self, numbers):
        raise NotImplementedError("Subclasses must implement this method")
        

    @staticmethod
    def swap(numbers, i, j):
        numbers[i], numbers[j] = numbers[j], numbers[i]

    @staticmethod
    def print_info(numbers):
        print(numbers)


class BubbleSort(SortStrategy):
    def sort(self, numbers):
        for i in range(len(numbers)):
            for j in range(len(numbers) - 1):
                if numbers[j] > numbers[j + 1]:
                    self.swap(numbers, j, j + 1)
        print('Bubble sort: ', end='')
        self.print_info(numbers)


class SelectionSort(SortStrategy):
    def sort(self, numbers):
        for i in range(len(numbers)):
            min_index = i
            for j in range(i + 1, len(numbers)):
                if numbers[j] < numbers[min_index]:
                    min_index = j
            self.swap(numbers, i, min_index)
        print('Selection sort: ', end='')
        self.print_info(numbers)


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort(self, numbers):
        self.strategy.sort(numbers)


if __name__ == '__main__':
    numbers = [10, 2, 5, 7, 3, 4, 1, 6, 8, 9]

    bobble_sort = BubbleSort()
    selection_sort = SelectionSort()

    context = Context(bobble_sort)
    context.sort(numbers)

    context.set_strategy(selection_sort)
    context.sort(numbers)
