from oper import Oper
from stack import Stack

if __name__ == "__main__":
    # price = float(input("Введите цену:"))
    # var_1 = Oper(10)
    # var_2 = Oper(0)
    #
    # # book = Book(price=price)
    # if var_1:
    #     print(f"var_1 is True")
    # if not var_2:
    #     print(f"var_2 is True")
    # else:
    #     print(f"var_2 is False")
    #
    # print(book.get_data())
    # if var_1 < "Hello":
    #     pass

    # var_3 = var_1 + (- var_2)
    stc = Stack()
    stc.push(1)
    stc.push(2)
    stc.push(3)
    print(f"{3} = {stc.indexOf(3)} позиция")
    stc[7] = 10
    print(f"Zero-Count = {stc.countOf(0)}")
    while stc.size >= 0:
        print(stc.pop())
