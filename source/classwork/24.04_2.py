


def roman_to_int(example):
    roman_num = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "l" : 50,
        "C" : 100
    }

    arab = list()


    for elem in reversed(example):
        if elem in roman_num.keys():
            arab.append(roman_num.values())

    return arab


def main():
    example = input(f"Введите римское число: ")
    res = roman_to_int(example)
    print(res)
if __name__ == "__main__":
    main()