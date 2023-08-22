# **Процедурное программирование:
# Разбиение массива на подмассивы:
# Задание: Напишите функцию, которая принимает массив чисел и значение X. 
# Функция должна возвращать массив подмассивов так, чтобы сумма чисел в каждом подмассиве была меньше или равна X.
# Входные данные:Массив чисел длиной N.Число X.
# Выходные данные:Массив подмассивов.


def split_array(arr, x):
    result = []
    current_sum = 0
    current_array = []
    for num in arr:
        if current_sum + num > x:
            result.append(current_array)
            current_array = []
            current_sum = 0
        current_array.append(num)
        current_sum += num
    result.append(current_array)
    return result



arr = [1, 2, 3, 4, 5, 6, 4, 8, 1]
x = 10

result = split_array(arr, x)
print(result)