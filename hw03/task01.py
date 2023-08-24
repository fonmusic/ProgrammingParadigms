"""
Фабричный метод:
Реализуйте паттерн Фабричный метод на языке Python для создания геометрических фигур.
Создайте класс ShapeFactory, имеющий метод create_shape(), который возвращает объекты различных геометрических фигур.
"""


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == 'circle':
            return Circle()
        elif shape_type == 'square':
            return Square()
        elif shape_type == 'triangle':
            return Triangle()
        else:
            raise ValueError(f'Unknown shape type: {shape_type}')


class Circle:
    @staticmethod
    def print_info():
        print("I am a circle")


class Square:
    @staticmethod
    def print_info():
        print("I am a square")


class Triangle:
    @staticmethod
    def print_info():
        print("I am a triangle")


if __name__ == '__main__':
    ShapeFactory.create_shape('circle').print_info()
    ShapeFactory.create_shape('square').print_info()
    ShapeFactory.create_shape('triangle').print_info()

    try:
        ShapeFactory.create_shape('rectangle').print_info()
    except ValueError as e:
        print(e)
