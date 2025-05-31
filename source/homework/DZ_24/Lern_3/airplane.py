class Airplane:
    __type_air = ""
    __passengers = 0
    __max_places = 0

    def __init__(self,type_air = "",passengers = 0,max_places = 0):
        self.__type_air = type_air
        self.__passengers = passengers
        self.__max_places = max_places

    def __del__(self):
        pass

    def get_type(self):
        return self.__type_air

    def set_type(self,type_air):
        self.__type_air = type_air

    def get_passenger(self):
        return self.__passengers

    def set_passenger(self,passengers):
        self.__passengers = passengers

    def get_max_places(self):
        return self.__max_places

    def set_max_places(self,max_places):
        self.__max_places = max_places


    def __eq__(self, other):
        if isinstance(other,Airplane):
            if len(self.__type_air) == len(other.__type_air):
                return f"Типы самолетов идентичны."
            else:
                return f"Самолеты относятся к разным типам"
        return False


    def __add__(self, other):
        if isinstance(other,Airplane):
            return Airplane(type_air=self.__type_air,passengers =self.__passengers + other.__passengers,
                            max_places = self.__max_places)
        elif isinstance(other,int):
            return Airplane(type_air=self.__type_air,passengers =self.__passengers + other,
                            max_places = self.__max_places)
        raise f"Ошибка типов"


    def __sub__(self, other):
        if isinstance(other,Airplane):
            return Airplane(type_air=self.__type_air, passengers=self.__passengers - other.__passengers,
                            max_places=self.__max_places)
        elif isinstance(other, int):
            return Airplane(type_air=self.__type_air, passengers=self.__passengers - other,
                            max_places=self.__max_places)
        raise f"Ошибка типов"

    def __iadd__(self, other):
        if isinstance(other,int):
            self.__passengers +=other
            return self
        raise f"Ошибка типов"

    def __isub__(self, other):
        if isinstance(other,int):
            self.__passengers -=other
            return self
        raise f"Ошибка типов"

    def __gt__(self, other):
        if isinstance(other,Airplane):
            if self.__max_places > other.__max_places:
                return (f"Количество мест самолета типа {self.__type_air},"
                        f" больше чем у самолета типа {other.__type_air}")
            else:
                return f"Тут поменьше мест..."
        raise "Ошибка типов"


    def __lt__(self, other):
        if isinstance(other,Airplane):
            if self.__max_places < other.__max_places:
                return (f"Количество мест самолета типа {self.__type_air},"
                        f" меньше чем у самолета типа {other.__type_air}")
            else:
                return f"Кажется мест больше, чем ожидалось"
        raise f"Ошибка типов"


    def __ge__(self, other):
        if isinstance(other,Airplane):
            return self.__max_places >= other.__max_places
        raise f"Ошибка типов"

    def __le__(self, other):
        if isinstance(other,Airplane):
            return self.__max_places <= other.__max_places
        raise f"Ошибка типов"




    def __str__(self):
        return (f"Тип самолета: {self.__type_air}\n"
                f"Количество пассажиров: {self.__passengers}\n"
                f"Максимальное количество мест: {self.__max_places} ")




