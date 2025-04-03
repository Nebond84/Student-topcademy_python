def summary_numbs(first,sign,second):
    res = 0
    if sign == "+":
        res = first + second
    return res


def main():

    first = int(input(f"Введите первое число: "))
    sign = input(f"Введите знак: ")
    second = int(input(f"Введите второе число: "))
    res = (summary_numbs(first,sign,second))
    print(f"{first} {sign} {second} = {res}")




if __name__ == "__main__":
    main()