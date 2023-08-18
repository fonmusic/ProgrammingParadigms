# Декларативное программирование:
# Задача 8: Вычисление суммы цифр числа. Напишите программу, которая вычисляет сумму всех цифр заданного числа,
# используя математические операции и деление нацело.

def sum_of_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum


result = sum_of_digits(12345)
print(result)