class Stadion:
    __name = str()
    __year = int(0)
    __country = str()
    __city = str()
    __capacity = int(0)

    def __init__(self, name = "Название",
                       year = 0,
                       country = "Страна",
                       city = "Город",
                       capacity = 0,
                 ):
        self.__name = name
        self.__year = year
        self.__country = country
        self.__city = city
        self.__capacity = capacity
        self.__add_attr = {}
    print(f"Был создан объект")


    def __del__(self):
        print(f"Объект был удален из памяти")

    def input_data(self,name = None,
                        year = None,
                        country = None,
                        city = None,
                        capacity = None
                   ):
        self.__name = name if name is not None else self.__name
        self.__year = year if year is not None else self.__year
        self.__country = country if country is not None else self.__country
        self.__city = city if city is not None else self.__city
        self.__capacity = capacity if capacity is not None else self.__capacity


    def add_atr(self,atr,atr_val):
       self.__add_attr[atr] = atr_val


    def output_file(self,output_file):
        with open(output_file, "a", encoding="utf-8")as f:
            f.write(self.get_data())


    def get_data(self):
        data = (f"\n\n\tСтадион - {self.__name}\n" 
            f"Год постройки - {self.__year} год\n"
            f"Страна - {self.__country}\n"
            f"Город - {self.__city}\n"
            f"Вместимость - {self.__capacity} человек\n")
        for atr, atr_val in self.__add_attr.items():
            data += f"{atr} - {atr_val}\n"
        return data


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name = None):
        if name is not None:
            self.__name = name


    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year = None):
        if year is not None:
            self.__year = year


    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country = None):
        if country is not None:
            self.__country = country


    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city = None):
        if city is not None:
            self.__city = city


    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity = None):
        if capacity is not None:
            self.__capacity = capacity







