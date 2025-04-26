
def menu():
    menu = (f"Показать список оценок : 1\n"
            f"Пересдача : 2\n"
            f"Подсчет стипендии : 3\n"
            f"Упорядочить оценки : 4\n"
            f"Выход : 5")

    return str(menu)


def print_rating(list_of_ratings):
    new_list = []
    for index,rating in enumerate(list_of_ratings):
        slot =f"{index+1}. оценка - {rating}"
        new_list.append(slot)
    for item in new_list:
        print(f"\t{item}")

    return str(new_list)

def update_rating(list_of_ratings):
    position = int(input(f"Выберите позицию для изменения оценки: "))

    new_rating = int(input(f"Введите оценку после пересдачи: "))
    list_of_ratings[position - 1] = new_rating
    return list_of_ratings

def scholarship_calculation(list_of_ratings):
    n = len(list_of_ratings)
    average = sum(list_of_ratings) / n
    return average

def insertion_sort(list_of_ratings):
    for i in range(1,len(list_of_ratings)):
        key = list_of_ratings[i]
        j = i - 1
        while j >= 0 and list_of_ratings[j] > key:
            list_of_ratings[j + 1] = list_of_ratings[j]
            j -= 1
            list_of_ratings[j + 1] = key
    return list_of_ratings



def main():
    count = 0
    list_of_ratings = []
    while count <10:
        ratings = int(input(f"Введите 10 оценок от 1 до 12, для выхода нажмите 0  : "))
        if 0 < ratings <= 12:
            list_of_ratings.append(ratings)
            count += 1
            print_rating(list_of_ratings)
        elif ratings == 0:
            exit()
        else:
            print(f"Введите корректную оценку!")
    while True:
        print(f"=======================================\n")
        print(menu())
        print(f"=======================================")
        choice = int(input(f"Выберите пункт меню: "))
        if choice <= 5:
            if choice == 1:
                print_rating(list_of_ratings)
                print(f"===================================")
            if choice == 2:
                update_rating(list_of_ratings)
                print_rating(list_of_ratings)
            if choice == 3:
                res = scholarship_calculation(list_of_ratings)
                if res < 10.7:
                    print(f"\n\n\t{res} - Стипендия не выходит!\n\n")
                    print(f"===================================")
                else:
                    print(f"\n\n\t{res} - Стипендия выходит!\n\n")
                    print(f"===================================")
            if choice == 4:
                insertion_sort(list_of_ratings)
                (print_rating(list_of_ratings))
                print(f"===================================")
            if choice == 5:
                break
        else:
            print(f"\n\n\t\tВведите корректный пункт меню!\n\n")




if __name__ == "__main__":
    main()