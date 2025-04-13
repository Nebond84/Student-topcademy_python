def find_divisor(first_number,second_number):
    if second_number == 0:
        return first_number
    else:
        return find_divisor(second_number,(first_number % second_number))


def main():
    first_number,second_number = map(int,input(f"Введите два числа через запятую: ").split(","))
    result = find_divisor(first_number,second_number)
    print(f"Наибольший делитель чисел: {first_number} и {second_number} равен - {result}")

if __name__ == "__main__":
    main()
