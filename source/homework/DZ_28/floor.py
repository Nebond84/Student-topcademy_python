from home import Home


class Floor(Home):
    __number_of_rooms = 0
    __number_of_bathrooms = 0


    def __init__(self,area,
                 input_power,
                 number_of_rooms,
                 number_of_bathrooms):
        self.__number_of_rooms = number_of_rooms
        self.__number_of_bathrooms = number_of_bathrooms
        super().__int__(area,input_power)

    def __del__(self):
        pass

    @property
    def rooms(self):
        return f"Количество комнат - {self.__number_of_rooms}"

    @rooms.setter
    def rooms(self,number_of_rooms):
        if number_of_rooms > 0:
            if type(number_of_rooms) is int:
                self.__number_of_rooms = number_of_rooms
            else:
                raise ValueError (f"Ожидается число!")
        else:
            raise ValueError (f"Количество комнат должно быть больше 0 ")


    @property
    def bathrooms(self):
        return f"Количество санузлов - {self.__number_of_bathrooms}"

    @bathrooms.setter
    def bathrooms(self,number_of_bathrooms):
        if number_of_bathrooms > 0:
            if type(number_of_bathrooms) is int:
                self.__number_of_bathrooms = number_of_bathrooms
            else:
                raise ValueError(f"Ожидается число!")
        else:
            raise ValueError(f"Количество комнат должно быть больше 0 ")


    def __str__(self):
        self.price+=(self.__number_of_rooms * 100000)+(self.__number_of_bathrooms * 60000)
        return (f"Первый Этаж:\n"
                f"Площадь - {self.area} кв.м.\n"
                f"Количество комнат - {self.__number_of_rooms}\n"
                f"Количество санузлов - {self.__number_of_bathrooms}\n"
                f"Входная мощность - {self.input_power} Квт.\n"
                f"Итоговая цена - {self.price} р.")
