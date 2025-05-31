class Car:
    __model_name = str()
    __year_of_issue = 1900
    __manufacturer = str()
    __engine_capacity = 0
    __color = str()
    __price = 0

    def __init__(self, model_name:str = "Название модели",
                       year_of_issue:int = 1900,
                       manufacturer:str = "Производитель",
                       engine_capacity: int = 0,
                       color: str = "Цвет",
                       price: int = 0
                 ):
        self.__model_name = model_name
        self.__year_of_issue = year_of_issue
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__color = color
        self.__price = price

    def __del__(self):
        pass


    def input_data(self,
                        model_name = None,
                        year_of_issue = None,
                        manufacturer = None,
                        engine_capacity = None,
                        color = None,
                        price = None
                    ):
        self.__model_name = model_name if model_name is not None else self.__model_name
        self.__year_of_issue = year_of_issue if year_of_issue is not None else self.__year_of_issue
        self.__manufacturer = manufacturer if manufacturer is not None else self.__manufacturer
        self.__engine_capacity = engine_capacity if engine_capacity is not None else self.__engine_capacity
        self.__color = color if color is not None else self.__color
        self.__price = price if price is not None else self.__price


    def get_info(self):
        return (f"\tАвтомобиль: {self.__model_name},\nгод выпуска: {self.__year_of_issue} год,\n"
              f"производитель: {self.__manufacturer},\nмощность двигателя: {self.__engine_capacity} л.с.,\n"
              f"цвет: {self.__color},\nцена: {self.__price}\n\n")


    @property
    def model_name(self):
        return self.__model_name

    @model_name.setter
    def model_name(self,model_name = None):
        if model_name != None:
            self.__model_name = model_name

    @property
    def year_of_issue(self):
        return self.__year_of_issue

    @year_of_issue.setter
    def year_of_issue(self, year_of_issue = None):
        if year_of_issue != None:
            self.__year_of_issue = year_of_issue

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer = None):
        if manufacturer != None:
            self.__manufacturer = manufacturer


    @property
    def engine_capacity(self):
        return self.__engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, engine_capacity = None):
        if engine_capacity != None:
            self.__engine_capacity = engine_capacity

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color = None):
        if color != None:
            self.__color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price = None):
        if price != None:
            self.__price = price






