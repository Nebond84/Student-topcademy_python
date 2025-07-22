import psycopg2
from _datetime import datetime

class Task:
    __description = str()
    __start_task = datetime.date
    __end_task = datetime.date
    __project_title = str()

    def __init__(self,
                 description = None,
                 start_task = None,
                 end_task = None,
                 project_title = None):
        self.__description = description
        self.__start_task = start_task
        self.__end_task = end_task
        self.__project_title = project_title

    def __del__(self):
        pass

    def input_task(self):
        description = input(f"Описание задачи: ")
        if not description or not isinstance(description, str) or not description.strip():
            raise ValueError(f"Поле 'Описание' не может быть пустым и должно быть строкой!")
        self.__description = description.strip()

        start_task = input(f"Укажите дату начала выполнения задачи: ")
        if start_task is not None:
            try:
                datetime.strptime(start_task, "%d-%m-%Y")
                self.__start_task = start_task
            except ValueError:
                raise ValueError(f"Дата должна быть в формате дд-мм-гггг!")


        end_task = input(f"Укажите дату выполнения задачи (если установлена): ")
        if not end_task.strip():

            self.__end_task = None
        else:
            try:
                datetime.strptime(end_task, "%d-%m-%Y")
                self.__end_task = end_task
            except ValueError:
                raise ValueError(f"Дата должна быть в формате дд-мм-гггг!")



        project_title = input(f"Укажите название проекта: ")
        if not project_title or not isinstance(project_title, str) or not project_title.strip():
            raise ValueError(f"Поле 'Имя проекта' не может быть пустым и должно быть строкой!")
        self.__project_title = project_title.strip()

    def save_to_db(self, connect):
        with psycopg2.connect(**connect) as connect:
            with connect.cursor() as cursor:
                sql = """
                INSERT INTO task(description,start_task,end_task,project_id)
                VALUES(%s,%s,%s,(select id from project where title = %s))
                """
                cursor.execute(sql, (self.__description,
                                     self.__start_task,
                                     self.__end_task,
                                     self.__project_title))
                connect.commit()

    @property
    def description(self):
        return self.__description

    @property
    def start_task(self):
        return self.__start_task

    @property
    def end_task(self):
        return self.__end_task

    @property
    def project_title(self):
        return self.__project_title


    def __str__(self):
        return (f"Описание задачи: {self.__description}\n"
                f"Дата начала выполнения задачи: {self.__start_task}\n"
                f"Дата выполнения задачи: {self.__end_task}\n"
                f"Название проекта: {self.__project_title}")