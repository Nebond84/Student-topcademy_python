
class Stack:

    def __init__(self):
        self.lst = list()

    def __del__(self):
        pass

    def push_stack(self,elem):
        self.lst.append(elem)

    def pop_stack(self,elem):
        if elem in stack:
            self.lst.pop(elem)








if __name__ == "__main__":
    stack = Stack()
    while True:
        elem = int(input(f"Введите числа: "))
        if elem == -1:
            break
        else:
            stack.push_stack(elem)
            print(len(stack.lst))

        # del_elem =
        #     print(stack.lst)


