class Rome:
    __rome_num = ""
    __roman_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "l": 50,
            "C": 100
        }


    def __init__(self,rome_num):
        self.__rome_num = rome_num

    def __del__(self):
        pass

    def roman_to_int(self,rome_num):
        arabian = list()
        for elem in rome_num:
            if elem in self.__roman_num.keys():
                arabian += (self.__roman_num.values())
        # self.__value = self.__arabian
        print(arabian)


        return self.__rome_num


if __name__ == "__main__":

    num1 = Rome(rome_num="X")
    print(num1.roman_to_int(rome_num="X"))