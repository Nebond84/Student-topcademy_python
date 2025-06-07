class Ship:
    __name = ""
    __chip_type = ""
    __top_calibre = 0
    __displacement = 0.0
    __crew = 0


    def __init__(self,
                 name,
                 chip_type,
                 top_calibre,
                 displacement,
                 crew):
        self.__name = name
        self.__chip_type = chip_type
        self.__top_calibre = top_calibre
        self.__displacement = displacement
        self.__crew = crew


    def __del__(self):
        pass

    




