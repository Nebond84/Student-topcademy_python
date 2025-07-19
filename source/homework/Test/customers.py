
import re
import psycopg2

class Customer:
    __name = str()
    __contact = str()
    __telephone_number = str()

    def __init__(self,
                 name = None,
                 contact = None,
                 __telephone_number = None):
        self.__name = name
        self.__contact = contact
        self.__telephone_number = __telephone_number


    def __del__(self):
        pass


    def input_customer(self):
        name = input(f"Введите название организации заказчика: ")
        if not name or not isinstance(name, str) or not name.strip():
            raise ValueError(f"Поле 'Имя' не может быть пустым и должно быть строкой!")
        self.__name = name.strip()

        contact = input(f"Введите Фамилию и Имя заказчика: ")
        if not contact or not isinstance(contact,str) or not contact.strip():
            raise ValueError(f"Поле 'Контакт' не может быть пустым и должно быть строкой!")
        self.__contact = contact.strip()

        telephone_number = input(f"Укажите телефон в формате +7хххххххххх: ")
        if telephone_number is not None:
            if not re.match(r'^\+7\d{10}$', telephone_number):
                raise ValueError(f"Телефон должен быть в формате +7XXXXXXXXXX (11 цифр)!")
            self.__telephone_number = telephone_number


    def save_to_db(self,connect):
        with psycopg2.connect(**connect) as connect:
            with connect.cursor() as cursor:
                sql = """
                INSERT INTO customer(name,contact,telephone_number)
                VALUES(%s,%s,%s)
                """
                cursor.execute(sql,(self.__name,self.__contact,self.__telephone_number))
                connect.commit()

    @property
    def name(self):
        return self.__name

    @property
    def contact(self):
        return self.__contact

    @property
    def telephone_number(self):
        return self.__telephone_number

    def __str__(self):
        return (f"Название организации: {self.__name}\n"
                f"Контактный представитель организации: {self.__contact}\n"
                f"Номер телефона: {self.__telephone_number}")

