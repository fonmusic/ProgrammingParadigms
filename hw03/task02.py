"""
Адаптер:
Создайте класс ElectricSocket, который имеет метод supply_electricity(voltage).
Реализуйте класс USPlugAdapter, который адаптирует розетку стандарта США к европейскому стандарту.
Создайте объекты и продемонстрируйте передачу электроэнергии через адаптер.
"""


class ElectricSocket:
    def supply_electricity(self, voltage):
        return voltage


class USPlugAdapter(ElectricSocket):
    def __init__(self, voltage):
        self.voltage = voltage

    def supply_electricity(self, voltage):
        return self.voltage


if __name__ == '__main__':
    socket = ElectricSocket()
    print(f'Electricity: {socket.supply_electricity(220)}V')

    adapter = USPlugAdapter(110)
    print(f'Electricity: {adapter.supply_electricity(220)}V')
