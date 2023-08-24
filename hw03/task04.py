"""
Декоратор:
Создайте класс Coffee с методом cost(), возвращающим стоимость кофе.
Реализуйте декораторы Sugar и Milk, которые добавляют сахар и молоко к кофе, соответственно.
Создайте объект кофе и последовательно примените к нему декораторы, затем выведите общую стоимость.
"""


class Coffee:
    def cost(self):
        return 90


class Sugar:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 10


class Milk:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 20


if __name__ == '__main__':
    coffee = Coffee()
    print(f'Coffee: {coffee.cost()}')

    coffee = Sugar(coffee)
    print(f'Coffee with sugar: {coffee.cost()}')

    coffee = Milk(coffee)
    print(f'Coffee with sugar and milk: {coffee.cost()}')
