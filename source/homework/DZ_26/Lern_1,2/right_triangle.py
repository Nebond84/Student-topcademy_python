from figure import Figure


class RightTriangle(Figure):
    __base = 0.0
    __height = 0.0

    def __init__(self,base,height):
        self.__base = base
        self.__height = height

    def __del__(self):
        pass

    def area(self):
        return 0.5 * self.__base * self.__height

    def __str__(self):
        return f"Треугольник имеет площадь: {int(self.area())}"