from circle import Circle

if __name__ == "__main__":
    c1 = Circle(9)
    c2 = Circle(6)
    print(c1 == c2)
    print(c1 > c2)
    print(c1 < c2)
    print(c1 <= c2)
    print(c1 >= c2)
    c3 = (c1 + 4)
    print(c3)
    c4 = c2-3
    print(c4)
    c1 += 5
    print(c1)
    c2 -= 2
    print(c2)
