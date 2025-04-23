import random
import source


def main():
    number_list =[]
    for i in range(30):
        number_list.append(random.randint(-128,500))
    print(number_list)
    min_num = source.min_nums(number_list)
    max_num = source.max_nums(number_list)
    positive_count = source.positive_nums(number_list)
    negative_count = source.negative_nums(number_list)
    zero_count = source.zero_nums(number_list)
    print(f"Минимальный элемент: {min_num}\nМаксимальный элемент: {max_num}\n"
          f"Количество положительных элементов: {positive_count}\n"
          f"Количество отрицательных элементов: {negative_count}\n"
          f"Количество нулей: {zero_count}")
if __name__ == "__main__":
    main()