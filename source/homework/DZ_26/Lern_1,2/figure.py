import abc
import math

class Figure(abc.ABC):


    @abc.abstractmethod
    def area(self):
        pass

    def __int__(self):
        return int(self.area())

