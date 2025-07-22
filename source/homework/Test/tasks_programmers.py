import psycopg2

class TaskProgrammer:
    __task_name = str()
    __programmer_name = str()
    __project_name = str()

    def __init__(self,
                 task_name = None,
                 programmer_name = None,
                 project_name = None):
        self.__task_name = task_name
        self.__programmer_name = programmer_name
        self.__project_name = project_name

    def __del__(self):
        pass

    def input_task_programmer(self):
        task_name = input(f"Укажите название задачи: ")
        if not task_name or not isinstance(task_name, str) or not task_name.strip():
            raise ValueError(f"Поле 'Задача' не может быть пустым и должно быть строкой!")
        self.__task_name = task_name.strip()

        programmer_name = input(f"Укажите программиста для это задачи: ")
        if not programmer_name or not isinstance(programmer_name, str) or not task_name.strip():
            raise ValueError(f"Поле 'Программист' не может быть пустым и должно быть строкой!")
        self.__programmer_name = programmer_name.strip()

        project_name = input(f"Укажите название проекта: ")
        if not project_name or not isinstance(programmer_name, str) or not project_name.strip():
            raise ValueError(f"Поле 'Проект' не может быть пустым и должно быть строкой!")
        self.__project_name = project_name.strip()

    def save_to_db(self, connect):
        with psycopg2.connect(**connect) as connect:
            with connect.cursor() as cursor:
                sql = """
                INSERT INTO TaskProgrammer(task_id,programmer_id)
                VALUES((select id from task where description = %s
		        and project_id = (select id from project where title = %s) LIMIT 1),
		        (select id from programmer where name = %s))
                """
                cursor.execute(sql, (self.__task_name,
                                     self.__project_name,
                                     self.__programmer_name))
                connect.commit()

    @property
    def task_name(self):
        return self.__task_name

    @property
    def project_name(self):
        return self.__project_name

    @property
    def programmer_name(self):
        return self.__programmer_name

    def __str__(self):
        return (f"Программисту {self.__programmer_name},\n"
                f"добавлена задача - {self.__task_name}")