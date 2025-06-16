import abc

class Home(abc.ABC):
    __area = 0.0
    __input_power = 0.0
    __price = 0


    def __int__(self,area,input_power):
        self._area = area
        self.__input_power = input_power
        self.__price +=(input_power * 2500)


    def __del__(self):
        pass


    @property
    def area(self):
        return self._area



    @property
    def input_power(self):
        return self.__input_power

    @input_power.setter
    def input_power(self, input_power):
        difference = input_power - self.__input_power
        self.price += (difference * 2500)
        self.__input_power = input_power

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


    @abc.abstractmethod
    def __str__(self):
        return f""
