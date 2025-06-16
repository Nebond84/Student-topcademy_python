from home import Home


class Roof(Home):
    __type_roof = ""
    __satellite_dish = "Нет"


    def __init__(self,area,
                 input_power,
                 type_roof):

        self._roofs = {"Односкатная": 4000,
                       "Двускатная": 6000,
                       "Конверт": 9000,
                       "Шатровая": 7000}
        super().__int__(area,input_power)
        self.__type_roof = type_roof if type_roof in self._roofs else None
        self.__satellite_dish = "Нет"
        self.price += self._roofs[type_roof] * area


    def __del__(self):
        pass

    @property
    def type_roof(self):
        return f"Тип крыши: {self.__type_roof}"

    @type_roof.setter
    def type_roof(self,type_roof):
        if type(type_roof) is str:
            current_roof = self.__type_roof
            if type_roof != self.__type_roof:
                if type_roof in self._roofs:
                    self.price -= self._roofs[current_roof] * self.area
                    self.__type_roof = type_roof
                    self.price += self._roofs[type_roof] * self.area
                else:
                    raise ValueError (f"Ожидается: Односкатная, Двускатная,"
                                      f"Конверт, Шатровая")
            else:
                raise ValueError (f"Уже выбрана")
        else:
            raise ValueError (f"Ожидается строка")

    @property
    def satellite(self):
        return self.__satellite_dish

    @satellite.setter
    def satellite(self,wish):
        if wish is not None and wish == "Да":
            if self.__satellite_dish != "Да":
                self.__satellite_dish = wish
                self.price += 12000
            else:
                raise ValueError (f"Уже установлена!")
        elif wish is not None and wish == "Нет":
            if self.__satellite_dish != "Нет":
                self.__satellite_dish = wish
                self.price -= 12000
            else:
                raise ValueError (f"Её и так нет!")
        else:
            raise ValueError (f"Ожидается Да или Нет")





    def __str__(self):
            return (f"Крыша:\n"
                    f"Тип крыши: {self.__type_roof}\n"
                    f"Площадь:  {self.area} кв.м.\n"
                    f"Входная мощность: {self.input_power} Квт.\n"
                    f"Спутниковая антенна: {self.__satellite_dish}\n"
                    f"Итоговая цена: {self.price} р.")