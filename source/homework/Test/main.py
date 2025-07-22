from project_manager import ProjectManager
from customers import Customer
from projects import Project
from programmers import Programmer
from tasks import Task
from tasks_programmers import TaskProgrammer
import select

connect = {
    "user": 'postgres',
    "password": '123',
    "host": 'localhost',
    "port": 5432,
    "dbname": 'test'
}

def top_menu():
    menu =(f"\tОсновное меню.\n"
           f"======================================\n"
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
            f"Добавить задачу - 5\n"
            f"Задача и программист - 6\n"
            f"Выход - 7")
    return data

def select_menu():
    sel = (f"\tКакая информация вас интересует?\n"
           f"======================================\n"
           f"Отобразить всю базу данных - 1\n")
    return sel

if __name__ == "__main__":
    while True:
        print(top_menu())
        choice = input(f"Выберете пункт меню: ")
        if choice == "1":
            print(select_menu())
            choice = input(f"Выберете пункт меню: ")
            if choice == "1":
                select.select_db(connect)
        elif choice == "2":
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
            if choice == "5":
                task = Task()
                try:
                    task.input_task()
                except ValueError as e:
                    print(f"Ошибка", e)
                else:
                    print(f"=====================")
                    print(f"Задача добавлена!\n"
                          f"{task}")
                    print(f"=====================")
                    task.save_to_db(connect)
            if choice == "6":
                task_programmer = TaskProgrammer()
                try:
                    task_programmer.input_task_programmer()
                except ValueError as e:
                    print(f"Ошибка", e)
                else:
                    print(f"=====================")
                    print(f"Задача добавлена!\n"
                          f"{task_programmer}")
                    print(f"=====================")
                    task_programmer.save_to_db(connect)
            if choice == "7":
                continue
        elif choice == "5":
            break
        else:
            print(f"Введите корректное значение!!!")
            print(f"=====================")





