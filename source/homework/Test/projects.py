
import psycopg2
from _datetime import datetime

class Project:
    __title = str()
    __start_project = datetime.date
    __end_project = datetime.date
    __customer_name = str()
    __manager_name = str()

    def __init__(self,
                 title = None,
                 start_project = None,
                 end_project = None,
                 customer_name = None,
                 manager_name = None):
        self.__title = title
        self.__start_project = start_project
        self.__end_project = end_project
        self.__customer_name = customer_name
        self.__manager_name = manager_name

    def __del__(self):
        pass


    def input_project(self):
        title = input(f"Название проекта: ")
        if not title or not isinstance(title, str) or not title.strip():
            raise ValueError(f"Поле 'Название проекта' не может быть пустым и должно быть строкой!")
        self.__title = title.strip()

        start_project = input(f"Укажите дату начала проекта: ")
        if start_project is not None:
            try:
                datetime.strptime(start_project, "%d-%m-%Y")
                self.__start_project = start_project
            except ValueError:
                raise ValueError(f"Дата должна быть в формате дд-мм-гггг!")

        end_project = input(f"Укажите дату окончания проекта: ")
        if end_project is not None:
            try:
                datetime.strptime(end_project, "%d-%m-%Y")
                self.__end_project = end_project
            except ValueError:
                raise ValueError(f"Дата должна быть в формате дд-мм-гггг!")

        customer_name = input(f"Укажите заказчика: ")
        if not customer_name or not isinstance(customer_name, str) or not customer_name.strip():
            raise ValueError(f"Поле 'Имя' не может быть пустым и должно быть строкой!")
        self.__customer_name = customer_name.strip()

        manager_name = input(f"Укажите менеджера: ")
        if not manager_name or not isinstance(manager_name, str) or not manager_name.strip():
            raise ValueError(f"Поле 'Имя' не может быть пустым и должно быть строкой!")
        self.__manager_name = manager_name.strip()



    def save_to_db(self,connect):
        with psycopg2.connect(**connect) as connect:
            with connect.cursor() as cursor:
                sql = """
                INSERT INTO project(title,start_project,end_project,customer_id,manager_id)
                VALUES(%s,%s,%s,(select id from customer where name = %s),
                (select id from project_manager where name = %s))
                """
                cursor.execute(sql,(self.__title,self.__start_project,
                                    self.__end_project,self.__customer_name,self.__manager_name))
                connect.commit()

    @property
    def title(self):
        return self.__title

    @property
    def start_project(self):
        return self.__start_project

    @property
    def end_project(self):
        return self.__end_project

    @property
    def customer_name(self):
        return self.__customer_name

    @property
    def manager_name(self):
        return self.__manager_name


    def __str__(self):
        return (f"Название проекта: {self.__title}\n"
                f"Дата начала проекта: {self.__start_project}\n"
                f"Дата окончания проекта: {self.__end_project}\n"
                f"Заказчик: {self.__customer_name}\n"
                f"Менеджер проекта: {self.__manager_name}")
