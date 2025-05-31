import math
class Circle:
    __radius = 0.0

    def __init__(self, radius):
        self.__radius = radius

    def __del__(self):
        pass

    def __eq__(self, other):
        if isinstance(other,Circle):
            if self.__radius == other.__radius:
                return f"Радиусы равны!"
            else:
                return f"Радиусы не равны!"
        return False

    def __gt__(self, other):
        if isinstance(other,Circle):
            if 2 * math.pi * self.__radius > 2 * math.pi * other.__radius:
                return (f"Окружность  с радиусом {self.__radius},"
                        f"больше окружности с радиусом {other.__radius}")
            return f"Нифига она не больше!"
        return False

    def __lt__(self, other):
        if isinstance(other,Circle):
            if 2 * math.pi * self.__radius < 2 * math.pi * other.__radius:
                return (f"Окружность с радиусом {self.__radius},"
                        f"меньше окружности с радиусом {other.__radius} ")
            return f"Нееет, она побольше будет...."
        return False

    def __le__(self, other):
        if isinstance(other,Circle):
            return 2 * math.pi * self.__radius <= 2 * math.pi * other.__radius
        return False

    def __ge__(self, other):
        if isinstance(other,Circle):
            return 2 * math.pi * self.__radius >= 2 * math.pi * other.__radius
        return False

    def __add__(self, other):
        if isinstance(other,(int,float)):
            return Circle(self.__radius + other)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other,(int,float)):
            return Circle(self.__radius - other)
        raise TypeError


    def __iadd__(self, other):
        if isinstance(other,(int,float)):
            self.__radius += other
            return self
        raise TypeError

    def __isub__(self, other):
        if isinstance(other,(int,float)):
            self.__radius -= other
            return  self
        raise TypeError


    def __str__(self):
        return f"Новый радиус окружности: {str(self.__radius)}"





