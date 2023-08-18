# Декларативное программирование:
# Задача 3: Вычисление факториала числа. Напишите программу, которая находит факториал 
# заданного числа N с использованием рекурсии или встроенных функций.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(5))