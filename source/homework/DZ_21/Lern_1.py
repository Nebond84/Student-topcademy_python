
import func

def insertion_sort(new_num_list):
    for i in range(1,len(new_num_list)):
        key = new_num_list[i]
        j = i - 1
        while j >= 0 and new_num_list[j] > key:
            new_num_list[j + 1] = new_num_list[j]
            j -= 1
            new_num_list[j + 1] = key
    return new_num_list

def search_num(sort_list,num):
    for index, element  in enumerate(sort_list):
        if num == element:
            return index
    return f"[-1] (отсутствует в списке)"




def main():
    num_list_1 = func.random_list()
    num_list_2 = func.random_list()
    num_list_3 = func.random_list()
    num_list_4 = func.random_list()
    new_num_list = num_list_1+num_list_2+num_list_3+num_list_4
    # sort_list =[]
    while True:

        var = input(f"Как отсортировать список:\n"
                    f"по возрастанию - нажмите 'y'\n"
                    f"по убыванию - нажмите 'n'\n"
                    f"для выхода нажмите '5':  "  )
        if var == "y":
            sort_list = insertion_sort(new_num_list)
            print(sort_list)
            num = int(input(f"\tвведите искомое число: \n\n"))
            res = search_num(sort_list, num)
            print(f"\tИскомый элемент находится в индексе - {res}\n\n")
        elif var == "n":
             sort_list= insertion_sort(new_num_list)[::-1]
             print(sort_list)
             num = int(input(f"\tвведите искомое число: \n\n"))
             res = search_num(sort_list, num)
             print(f"\tИскомый элемент находится в индексе - {res}\n\n")
        elif var == "5":
            break
        else:
            print(f"Введите корректную команду!!!")



if __name__ == "__main__":
    main()