"""
Монады: Реализуйте класс IO (ввод-вывод), который будет представлять действие ввода-вывода.
Создайте функцию-редуктор, которая будет принимать список IO и последовательно выполнять каждое действие,
сохраняя результаты в список.
"""


class IO:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        return func(self.value)


def read_file(file_name):
    with open(file_name, 'r') as file:
        return IO(file.read())


def write_file(file_name, text):
    with open(file_name, 'w') as file:
        return IO(file.write(text))


def print_text(text):
    print(text)
    return IO(text)


if __name__ == '__main__':
    # create file
    with open('test.txt', 'w') as file:
        file.write('Hello world!')
        
    result = IO(0) \
        .bind(lambda x: read_file('test.txt')) \
        .bind(lambda x: print_text(x)) \
        .bind(lambda x: write_file('test2.txt', x)) \
        .bind(lambda x: print_text(x))

    print(result)
