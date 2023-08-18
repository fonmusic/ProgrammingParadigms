# Императивное программирование:
# Задача 5: Поиск простых чисел. Напишите программу, которая находит все простые числа в заданном 
# диапазоне от 1 до N.

n = int(input("Введите число N: "))
for num in range(2, n+1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)