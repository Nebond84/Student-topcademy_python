from home import Home


class Roof(Home):
    __type_roof = ""
    __satellite_dish = ""


    def __init__(self,area,
                 input_power,
                 type_roof,
                 satellite_dish):
        super().__int__(area,input_power)
        self.__type_roof = type_roof
        self.__satellite_dish = satellite_dish

    def __del__(self):
        pass