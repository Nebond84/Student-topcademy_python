import psycopg2
from _datetime import datetime
import re

class Programmer:
    __name = str()
    __birthdate = datetime.date
    __phone = str()
    __skill_level = str()

    def __init__(self,
                name = None ,
                birthdate = None,
                 skill_level = None,
                phone = None):
        self.__name = name
        self.__birthdate = birthdate
        self.__skill_level = skill_level
        self.__phone = phone
        self._skill = ['junior', 'middle', 'senior']


    def __del__(self):
        pass

    def input_programmer(self):
        name = input(f"Фамилию и имя программиста: ")
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

        skill_level = input(f"Укажите уровень программиста(junior', 'middle', 'senior): ")
        if (not skill_level
                or not isinstance(skill_level, str)
                or not skill_level.strip()
                or not self._skill):
            raise ValueError(f"Поле 'Уровень' не может быть пустым и должно быть строкой,"
                             f" и принадлежать списку(junior', 'middle', 'senior)!")
        self.__skill_level = skill_level.strip()

        phone = input(f"Укажите телефон в формате +7хххххххххх: ")
        if phone is not None:
            if not re.match(r'^\+7\d{10}$', phone):
                raise ValueError(f"Телефон должен быть в формате +7XXXXXXXXXX (11 цифр)!")
            self.__phone = phone


    def save_to_db(self,connect):
        with psycopg2.connect(**connect) as connect:
            with connect.cursor() as cursor:
                sql = """
                INSERT INTO programmer(name,birthdate,skill_level,phone)
                VALUES(%s,%s,%s,%s)
                """
                cursor.execute(sql,(self.__name,self.__birthdate,self.__skill_level,self.__phone))
                connect.commit()

    @property
    def name(self):
        return self.__name

    @property
    def birthdate(self):
        return self.__birthdate

    @property
    def skill_level(self):
        return self.__skill_level

    @property
    def phone(self):
        return self.__phone

    def __str__(self):
        return(f"Фамилия и имя программиста: {self.__name}\n"
               f"Дата рождения: {self.__birthdate}\n"
               f"Уровень программиста: {self.__skill_level}\n"
               f"Телефон: {self.__phone}")



