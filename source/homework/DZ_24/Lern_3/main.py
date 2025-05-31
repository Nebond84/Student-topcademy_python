from airplane import Airplane
if __name__ == "__main__":
    air1 = Airplane("Широкофюзеляжный",124,853)
    air2 = Airplane("Узкофюзеляжный",200,295)

    print(air1 == air2)
    print("========================")
    print(air1)
    print("========================")
    print(air2)
    print("========================")
    air3 = air1 + 50
    print(air3)
    print("========================")
    air4 = air2 - 40
    print(air4)
    print("========================")
    air1 += 20
    print(air1)
    print("========================")
    air2 -= 100
    print(air2)
    print("========================")
    print(air1 > air2)
    print("========================")
    print(air2 < air1)
    print("========================")
    print(air1 >= air2)
    print("========================")
    print(air1 <= air2)

