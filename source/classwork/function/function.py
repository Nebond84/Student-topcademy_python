def functionPrint(lst : list):
    for elem in lst:
        print(f"Hello, {elem}", end="! | ")
    print()

def functionPrintRevers(lst : list):
    for elem in lst:
        print(f"{elem}, hello", end="! | ")
    print()

def getPrintFunction(reversFlag : bool):
    if reversFlag:
        return functionPrintRevers
    else:
        return functionPrint

def summer(First : int, Second: int) -> int:
    return First + Second

def minus(First : int, Second: int) -> int:
    return First - Second

def multiply(First : int, Second: int) -> int:
    return First * Second

def division(First : int, Second: int) -> int:
    if (not Second):
        return 0
    else:
        return First + Second

def steps(First : int, Second: int) -> int:
    return First ** Second

def stepsFromPlus(First : int , Second: int) -> int:
    result = First
    for i in range(1, Second):
        tmp = result
        for j in range(1, First + 1):
           tmp += result
        result = tmp
    return result

def getMathFunc(sign : str):
    match sign:
        case "+": return summer
        case "-": return minus
        case "*": return multiply
        case "/": return division
        case "^": return steps