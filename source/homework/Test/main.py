from project_manager import ProjectManager
from customers import Customer
from projects import Project
from programmers import Programmer

connect = {
    "user": 'postgres',
    "password": '123',
    "host": 'localhost',
    "port": 5432,
    "dbname": 'test'
}

def top_menu():
    menu =(f"\tОсновное меню.\n"
           f"Вывести информацию из Базы данных - 1\n"
           f"Добавить информацию в базу данных - 2\n"
           f"Обновить данные в базе - 3\n"
           f"Удалить данные из базы - 4\n"
           f"Выход - 5")
    return menu

def add_menu():
    data = (f"\tОбъекты для добавления в базу данных.\n"
            f"======================================\n"
            f"Добавить менеджера - 1\n"
            f"Добавить заказчика - 2\n"
            f"Добавить проект - 3\n"
            f"Добавить программиста - 4\n"
            f"Добавить задачу - 5\n")
    return data

if __name__ == "__main__":
    while True:
        print(top_menu())
        choice = input(f"Выберете пункт меню: ")
        if choice == "2":
            print(add_menu())
            choice = input(f"Выберете пункт меню: ")
            if choice == "1":
                project_manager = ProjectManager()
                try:
                    project_manager.input_manager()
                except ValueError as e:
                    print(f"Ошибка", e)
                else:
                    print(f"=====================")
                    print(f"Менеджер добавлен!\n"
                          f"{project_manager}")
                    print(f"=====================")
                    project_manager.save_to_db(connect)
            if choice == "2":
                customer = Customer()
                try:
                    customer.input_customer()
                except ValueError as e:
                    print(f"Ошибка", e)
                else:
                    print(f"=====================")
                    print(f"Заказчик добавлен!\n"
                          f"{customer}")
                    print(f"=====================")
                    customer.save_to_db(connect)
            if choice == "3":
                project = Project()
                try:
                    project.input_project()
                except ValueError as e:
                    print(f"Ошибка", e)
                else:
                    print(f"=====================")
                    print(f"Проект добавлен!\n"
                          f"{project}")
                    print(f"=====================")
                    project.save_to_db(connect)
            if choice == "4":
                programmer = Programmer()
                try:
                    programmer.input_programmer()
                except ValueError as e:
                    print(f"Ошибка", e)
                else:
                    print(f"=====================")
                    print(f"Программист добавлен!\n"
                          f"{programmer}")
                    print(f"=====================")
                    programmer.save_to_db(connect)
        elif choice == "5":
            break
        else:
            print(f"Введите корректное значение!!!")
            print(f"=====================")





