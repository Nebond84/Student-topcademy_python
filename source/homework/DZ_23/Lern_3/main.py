
from stadion import Stadion

def top_menu():
    menu = (f"\tОсновное меню.\n"
            f"Новый объект - 1\n"
            f"Открыть файл хранящий объекты - 3\n"
            f"Выход - 5\n")
    return menu

def sub_menu():
    menu = (f"\tМеню редактора!\n"
            f"Изменить название - 1\n"
            f"Изменить год - 2\n"
            f"Изменить страну - 3\n"
            f"Изменить город - 4\n"
            f"Изменить вместимость - 5\n"
            f"Сохранить в файл - 6\n"
            f"Добавить атрибут - 7\n"
            f"Выход в главное меню - 0")
    return menu


def show_file(file):
    with open(file, "r", encoding="utf-8") as f2:
        return f2.read()


def save_file(output_file):
    stadion.output_file(output_file)
    return


if __name__ == "__main__":
    # stadion = None
    while True:
        print(top_menu())
        choice = input(f"\tВыберите пункт меню: ")
        if choice == "1":
            name = input(f"Введите название стадиона: ")
            year = input(f"Укажите год постройки: ")
            country = input(f"Укажите страну: ")
            city = input(f"Укажите город: ")
            capacity = input(f"Укажите вместимость стадиона: ")

            stadion = Stadion(name = name,
                              year=year,
                              country=country,
                              city=city,
                              capacity=capacity)
            print(stadion.get_data())
            print(f"Сохранить - 'y', Изменить данные - 'r', Выход - 'n'")
            var = input(f"Выберите пункт меню: ")
            if var == "y":
                output_file = input(f"Укажите путь к файлу: ")
                save_file(output_file)
                # stadion.output_file(output_file)
                print(f"\n\tФайл успешно сохранен!")
                print(stadion.get_data())
            elif var == "r":
                while True:
                    print(sub_menu())
                    sub_var = input(f"Выберите действие: ")
                    if sub_var == "1":
                        name = input(f"Введите новое название: ")
                        stadion.name = name
                        print(f"Название успешно изменено на {name}")
                    elif sub_var == "2":
                        year = input(f"Введите новое значение: ")
                        stadion.year = year
                        print(f"Значение успешно изменено на {year}")
                    elif sub_var == "3":
                        country = input(f"Введите новое название страны: ")
                        stadion.country = country
                        print(f"Название страны успешно изменено на {country}")
                    elif sub_var == "4":
                        city = input(f"Введите новое название города: ")
                        stadion.city = city
                        print(f"Название города успешно изменено на {city}")
                    elif sub_var == "5":
                        capacity = input(f"Введите новое значение: ")
                        stadion.capacity = capacity
                        print(f"Значение успешно заменено на {capacity}")
                    elif sub_var == "6":
                        output_file = input(f"Укажите путь к файлу: ")
                        save_file(output_file)
                        # stadion.output_file(output_file)
                        print(f"\n\tФайл успешно сохранен!")
                        print(stadion.get_data())
                    elif sub_var == "7":
                        if stadion:
                            atr = input(f"Введите имя атрибута: ")
                            atr_val = input(f"Введите значение атрибута: ")
                            stadion.add_atr(atr,atr_val)
                            print(stadion.get_data())

                    elif sub_var == "0":
                        break
                    else:
                        print("_______Выберите корректный пункт меню!_______")

            elif var == "n":
                break
            else:
                print(f"______Введите корректное значение!_______\n")

        elif choice == "3":
            file = input(f"Укажите путь файла для просмотра: ")
            doc = show_file(file)
            print(doc)

        elif choice == "5":
            break
        else:
            print(f"______Введите корректное значение!_______\n")

