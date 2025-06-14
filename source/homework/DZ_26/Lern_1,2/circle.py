import math

from figure import Figure


class Circle(Figure):
    __radius = 0.0

    def __init__(self,radius):
        self.__radius = radius


    def __del__(self):
        pass

    def area(self):
        return math.pi * self.__radius ** 2


    def __str__(self):
        return f"Окружность имеет площадь: {int(self.area())}"