import random

def buble_sort(num_list):
    i = 1
    while i < len(num_list):
        if num_list[i] < num_list[i - 1]:
            num_list[i], num_list[i - 1] = num_list[i -1],num_list[i]
            j = i - 1
            while j > 0:
                if num_list[j] < num_list[j - 1]:
                    num_list[j], num_list[j - 1] = num_list[j - 1],num_list[j]
                else:
                    break
                j -= 1
            i -= 1
        i += 1
    return num_list

def main():
    num_list = []
    for i in range(30):
        num_list.append(random.randint(-128, 500))
    res = buble_sort(num_list)
    print(f"{res}")
if __name__ == "__main__":
    main()
