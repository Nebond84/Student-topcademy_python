from home import Home


class AdditionalBuildings(Home):
    __types_of_buildings = []


    def __init__(self,area,
                 input_power,
                 types_of_buildings):
        super().__int__(area, input_power)
        self.__types_of_buildings = types_of_buildings


    def __del__(self):
        pass
