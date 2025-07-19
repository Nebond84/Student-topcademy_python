from _datetime import datetime
import re
import psycopg2


class ProjectManager:
    __name = str()
    __birthdate = datetime.date
    __phone = str()

    def __init__(self,
                name = None ,
                birthdate = None,
                phone = None):
        self.__name = name
        self.__birthdate = birthdate
        self.__phone = phone


    def __del__(self):
        pass




    def input_manager(self):
        name = input(f"Фамилию и имя менеджера: ")
        if not name or not isinstance(name, str) or not name.strip():
            raise ValueError(f"Поле 'Имя' не может быть пустым и должно быть строкой!")
        self.__name = name.strip()
        birthdate = input(f"Введите год рождения в формате дд-мм-гггг: ")
        if birthdate is not None:
            try:
                datetime.strptime(birthdate, "%d-%m-%Y")
                self.__birthdate = birthdate
            except ValueError:
                raise ValueError(f"Дата рождения должна быть в формате дд-мм-гггг!")
        phone = input(f"Укажите телефон в формате +7хххххххххх: ")
        if phone is not None:
            if not re.match(r'^\+7\d{10}$', phone):
                raise ValueError(f"Телефон должен быть в формате +7XXXXXXXXXX (11 цифр)!")
            self.__phone = phone


    def save_to_db(self,connect):
        with psycopg2.connect(**connect) as connect:
            with connect.cursor() as cursor:
                sql = """
                INSERT INTO project_manager(name,birthdate,phone)
                VALUES(%s,%s,%s)
                """
                cursor.execute(sql,(self.__name,self.__birthdate,self.__phone))
                connect.commit()


    @property
    def name(self):
        return self.__name
    @property
    def birthdate(self):
        return self.__birthdate
    @property
    def phone(self):
        return self.__phone



    def __str__(self):
        return (f"Имя: {self.__name}\n"
                f"Дата рождения: {self.__birthdate}\n"
                f"Телефон: {self.__phone}")





