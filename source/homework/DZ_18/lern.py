def find_divisor(first_number,second_number):
    """
    Функция принимает два целых числа
    :param first_number: первое число
    :param second_number: второе число
    :return: возвращает наибольший делитель двух чисел
    """
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

for i in range(1,11):
    for j in range(1,10):
        res = i * j
        print(f"{i} * {j} = {res}")