from home import Home


class AdditionalBuildings(Home):
    __types_of_buildings = None


    def __init__(self,area,
                 input_power,
                 ):
        super().__int__(area, input_power)
        self._building = {"Гараж" : 400000,
                    "Беседка" : 150000,
                    "Баня" : 700000}
        self.__types_of_buildings = []



    def __del__(self):
        pass



    @property
    def building(self):
        return f"Установлены дополнительные строения: {", ".join(self.__types_of_buildings)}"


    def add_building(self,types_of_buildings):
        if type(types_of_buildings) is str:
            if types_of_buildings in self._building:
                if types_of_buildings is not self.__types_of_buildings:
                    self.__types_of_buildings.append(types_of_buildings)
                    self.price += self._building[types_of_buildings]
                else:
                    raise ValueError (f"Строение уже имеется")
            else:
                raise ValueError (f"Ожидается Гараж, Баня, Беседка")
        else:
            raise ValueError (f"Ожидается строка")

    def del_building(self,types_of_buildings):
        if type(types_of_buildings) is str:
            if types_of_buildings in self.__types_of_buildings:
                self.__types_of_buildings.remove(types_of_buildings)
                self.price -= self._building[types_of_buildings]
                return f"Строение {types_of_buildings}, удалено!"
            else:
                raise ValueError (f"Нет здесь этого!")
        else:
            raise ValueError (f"Ожидается строка!")


    def __str__(self):
        build = ", ".join(self.__types_of_buildings)
        return (f"Дополнительные строения:\n"
                f"Площадь дополнительных строений - {self.area}\n"
                f"Входная мощность - {self.input_power}\n"
                f"Размещены дополнительные строения - {build}\n"
                f"Итоговая цена - {self.price}")

