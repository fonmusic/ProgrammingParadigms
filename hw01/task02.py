# Императивное программирование:
# Задача 2: Поиск наименьшего числа в списке. Напишите программу, которая находит
# наименьшее число в заданном списке с помощью цикла.


numbers = [3, 7, 1, 9, 4, 2, 6, 8, 5]

smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number


print(smallest)