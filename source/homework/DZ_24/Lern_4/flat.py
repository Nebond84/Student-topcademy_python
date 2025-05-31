class Flat:
    __square = 0.0
    __price = 0

    def __init__(self,square = 0.0,price = 0.0):
        self.__square = square
        self.__price = price

    def __del__(self):
        pass

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self,square):
        self.__square = square

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __eq__(self, other):
        if isinstance(other,Flat):
            if self.__square == other.square:
                return f"Да"
            else:
                return f"Нет"
        raise f"Ошибка типов"

    def __ne__(self, other):
        if isinstance(other,Flat):
            if self.__square != other.square:
                return f"Да"
            else:
                return f"Нет"
        raise f"Ошибка типов"

    def __gt__(self, other):
        if isinstance(other,Flat):
            return self.__price > other.price
        raise f"Ошибка типов"

    def __lt__(self, other):
        if isinstance(other,Flat):
            return self.__price < other.price
        raise f"Ошибка типов"

    def __ge__(self, other):
        if isinstance(other,Flat):
            return self.__price >= other.price
        raise f"Ошибка типов"

    def __le__(self, other):
        if isinstance(other,Flat):
            return self.__price <= other.price
        raise f"Ошибка типов"

    def __str__(self):
        return (f"Квартира площадью: {self.__square} кв.м.,\n"
                f"Стоимость: {self.__price} р. ")
