from home import Home

class Basement(Home):
    __type_basement = ""
    __communication = []


    def __init__(self,area,
                input_power,
                type_basement,
                ):
        super().__int__(area,input_power)
        # self.__type_basement = type_basement
        self.__communication = []
        self._type_communication = {"Вода":40000,
                                     "Канализация":43000,
                                     "Газ":140000}
        self._basement = {"Ленточный":4000,
                          "Свайный":1200,
                          "Плитный":3500}

        if type_basement in self._basement:
            self.__type_basement  = type_basement
            self.price +=(self._basement[type_basement] * area)


    def __del__(self):
        pass

    @property
    def base(self):
        return self.__type_basement

    @base.setter
    def base(self,name):
        if type(name) is str:
            current_base = self.__type_basement
            if name != self.__type_basement:
                if name in self._basement:
                    self.price -= self._basement[current_base] * self.area
                    self.__type_basement = name
                    self.price += self._basement[name] * self.area
                else:
                    raise ValueError (f"Ожидается: Ленточный, Свайный, Плитный ")
            else:
                raise ValueError (f"Уже выбран!")
        else:
            raise ValueError (f"Ожидается строка")


    def add_commun(self,communication):
        if communication in self._type_communication:
            self.__communication.append(communication)
            self.price += self._type_communication[communication]
            return (f"Добавлена коммуникация: {communication}\n"
                    f"стоимостью - {self._type_communication[communication]} р.")
        else:
            raise ValueError (f"Ожидается - (Вода, Канализация, Газ)")

    def del_commun(self,communication):
        if communication in self._type_communication:
            self.__communication.remove(communication)
            self.price -= self._type_communication[communication]
            return (f"Удалена коммуникация: {communication}\n"
                    f"стоимостью - {self._type_communication[communication]} р.")
        else:
            raise ValueError (f"Ожидается - (Вода, Канализация, Газ)")


    def __str__(self):
        communication = ", ".join(self.__communication)
        return (f"Подвал:\n"
                f"Тип фундамента - {self.__type_basement}\n"
               f"Площадь - {self.area} м.кв\n"
               f"Подводимые коммуникации - {communication}\n"
               f"Входная мощность - {self.input_power} Квт\n"
                f"Итоговая цена - {self.price} рублей")
