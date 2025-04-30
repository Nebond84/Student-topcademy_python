import func

def unique(num_list_1,num_list_2,num_list_3,num_list_4):
    unique_list = set(num_list_1)^set(num_list_2)^set(num_list_3)^set(num_list_4)
    return unique_list

def insertion_sort(num_list_5):
    for i in range(1,len(num_list_5)):
        key = num_list_5[i]
        j = i - 1
        while j >= 0 and num_list_5[j] > key:
            num_list_5[j + 1] = num_list_5[j]
            j -= 1
            num_list_5[j + 1] = key
    return num_list_5

def binary_search(res,target):
    left,right = 0, len(res) -1
    increase = res[left]  < res[right]
    while left <= right:
        mid = (left + right) // 2
        if res[mid] == target:
            return mid
        if increase:
            if res[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if res[mid] > target:
                left = mid - 1
            else:
                right = mid + 1

    return -1





def main():
    num_list_1 = func.random_list()
    num_list_2 = func.random_list()
    num_list_3 = func.random_list()
    num_list_4 = func.random_list()


    num_list_5 = unique(num_list_1,num_list_2,num_list_3,num_list_4)
    num_list_5 = list(num_list_5)
    print(num_list_5)

    while True:
        var = input(f"Как отсортировать список:\n"
                    f"по возрастанию - нажмите 'y'\n"
                    f"по убыванию - нажмите 'n'\n"
                    f"для выхода нажмите '5':  ")
        if var == "y":
            res = insertion_sort(num_list_5)
            print(res)
            target = int(input(f"Введите искомый элемент: "))
            index = binary_search(res, target)
            print(f"\tИскомый элемент находится в индексе - {index}\n\n")
        elif var == "n":
            res = insertion_sort(num_list_5)[::-1]
            print(res)
            target = int(input(f"Введите искомый элемент: "))
            index = binary_search(res,target)
            print(f"\tИскомый элемент находится в индексе - {index}\n\n")
        elif var == "5":
            break
        else:
            print(f"Введите корректную команду!!!")

if __name__ == "__main__":
    main()