def calculate(arithmetic_expression):
    arithmetic_expression = arithmetic_expression.replace(" ","")
    temp = ""
    first_num = ""
    sign = ""
    second_num = ""
    for elem in arithmetic_expression:
        if elem in "+-/*":
            sign = elem
            first_num = int(temp)
            temp = ""
        else:
            temp += elem
    second_num = int(temp)

    if sign == "+":
        return first_num + second_num
    elif sign == "-":
        return first_num - second_num
    elif sign == "/":
        return first_num / second_num
    elif sign == "*":
        return first_num * second_num
    else:
        return f"неверный ввод"




def main():
    arithmetic_expression = input(f"Введите арифметическое выражение: ")
    res = calculate(arithmetic_expression)
    print(f"Решение: {arithmetic_expression} = {res}")

if __name__ == "__main__":
    main()