from figure import Figure


class Rectangle(Figure):
    __width = 0.0
    __height = 0.0

    def __init__(self,width,height):
        self.__width = width
        self.__height = height

    def __del__(self):
        pass

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"Прямоугольник имеет площадь: {int(self.area())}"
