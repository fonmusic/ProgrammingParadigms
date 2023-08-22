# Рекурсивное вычисление чисел Фибоначчи:
# Задание: Напишите рекурсивную функцию для вычисления n-того числа Фибоначчи.
# Входные данные:Число n.
# Выходные данные:n-тое число Фибоначчи.


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(5)) # выведет 5
print(fibonacci(10)) # выведет 55