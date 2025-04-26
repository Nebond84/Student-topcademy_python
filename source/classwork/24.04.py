
def brackets_bool(brackets):
    stack = list()
    for elem in brackets:
        if elem in "([{":
            stack.append(elem)
        elif elem == ")":
            if stack[len(stack) -1] == "(":
                stack.pop()
                continue
            else:
                return False
        elif elem == "]":
            if stack[len(stack) -1] == "[":
                stack.pop()
                continue
            else:
                return False
        elif elem == "}":
            if stack[len(stack)-1] == "{":
                stack.pop()
                continue
            else:
                return False
    return False if len(stack) else True


def main():
    brackets = input(f"Введите строку из скобок: ")
    res = brackets_bool(brackets)
    print(res)

if __name__ == "__main__":
    main()


