from figure import Figure


class Trapezoid(Figure):
    __base_1 = 0.0
    __base_2 = 0.0
    __height = 0.0

    def __init__(self,base_1,base_2,height):
        self.__base_1 = base_1 if base_1 > 0 else self.__base_1
        self.__base_2 = base_2 if base_2 > 0 else self.__base_2
        self.__height = height if height > 0 else self.__height

    def __del__(self):
        pass

    @property
    def base_1(self):
        return self.__base_1

    @base_1.setter
    def base_1(self,base_1):
        if base_1 > 0:
            if type(base_1) is float:
                self.__base_1 = base_1
            raise ValueError (f"Ожидается число с плавающей точкой")
        raise ValueError (f"Длинна не может быть отрицательная или равна - 0 ")

    @property
    def base_2(self):
        return self.__base_2

    @base_2.setter
    def base_2(self, base_2):
        if base_2 > 0:
            if type(base_2) is float:
                self.__base_2 = base_2
            raise ValueError(f"Ожидается число с плавающей точкой")
        raise ValueError(f"Длинна не может быть отрицательная или равна - 0 ")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height > 0:
            if type(height) is float:
                self.__height = height
            raise ValueError(f"Ожидается число с плавающей точкой")
        raise ValueError(f"Длинна не может быть отрицательная или равна - 0 ")


    def area(self):
        return 0.5 * self.__base_1 * self.__base_2


    def __str__(self):
        return f"Трапеция  имеет площадь: {int(self.area())} кв.мм."