# Роли в Университете:
#
# Студенты      - ФИО, Возраст, Группа
# Преподаватели - ФИО, Возраст, Кафедра
# Администрация - ФИО, Возраст, Должность

# Наследование - это возможность создания новой сущности (класса) на базе
# уже существующей сущности (другого класса)
# Наследование - это механизм языка, позволяющий передать механизмы
# от classA (родительский класс/superclass) в classB (наследник)

import abc  # Импортируем модуль abc для работы с абстрактными классами

# Определяем базовый класс Person
class Person(abc.ABC):
    __name = str()  # Приватное поле для хранения имени
    _age = 0  # Защищенное поле для хранения возраста
    _med_id = str()  # Защищенное поле для хранения медицинского ID

    # Конструктор класса, инициализирующий имя, возраст и медицинский ID
    def __init__(self,
                 name: str = "",
                 age: int = 0,
                 med_id: str = ""):
        self.__name = name  # Устанавливаем имя
        self._age = age  # Устанавливаем возраст
        self._med_id = med_id  # Устанавливаем медицинский ID

    def __del__(self):
        pass  # Метод деструктора, который можно переопределить при необходимости

    @property
    def med_id(self):
        return self._med_id  # Геттер для медицинского ID

    @med_id.setter
    def med_id(self, new_id: str):
        if len(new_id) == 0:  # Проверка на пустую строку
            return
        self._med_id = new_id  # Сеттер для медицинского ID

    @abc.abstractmethod
    def getMedId(self):
        pass  # Абстрактный метод, который должен быть реализован в подклассах

    def __str__(self):
        return f"Имя: {self.__name}\nВозраст: {self._age}"  # Строковое представление объекта

    def say_hello(self):
        return f"Привет, меня зовут {self.__name}"  # Метод для приветствия


# Класс Student наследуется от класса Person
from typing import final  # Импортируем final для предотвращения наследования

class Student(Person):
    __group = str()  # Приватное поле для хранения группы

    # Конструктор класса, инициализирующий имя, возраст и группу
    def __init__(self, name: str = "",
                       age: int = 0,
                       group: str = ""
                 ):
        super().__init__(name, age)  # Вызываем конструктор родительского класса
        self.__group = group  # Устанавливаем группу

    def __del__(self):
        pass  # Метод деструктора

    def say_hello(self):
        return f"{super().say_hello()}. {self.my_group()}"  # Приветствие с указанием группы

    def __str__(self):
        return f"{super().__str__()}\nГруппа: {self.__group}"  # Строковое представление с группой

    def my_group(self):
        return f"Я из группы {self.__group}"  # Метод для получения информации о группе

    def getMedId(self):
        return f"Мой ID - {self._med_id}"  # Метод для получения медицинского ID

    def func(self):
        self._age = 0  # Метод, который устанавливает возраст в 0

# Класс Teacher наследуется от класса Person
class Teacher(Person):
    _kafedra = str()  # Защищенное поле для хранения кафедры

    # Конструктор класса, инициализирующий имя, возраст и кафедру
    def __init__(self, name: str = "",
                       age: int = 0,
                       kafedra: str = ""
                 ):
        super().__init__(name, age)  # Вызываем конструктор родительского класса
        self._kafedra = kafedra  # Устанавливаем кафедру

    def __del__(self):
        pass  # Метод деструктора

    def my_job(self):
        return f"Я работаю на кафедре {self._kafedra}"  # Метод для получения информации о кафедре

    def say_hello(self):
         return f"{super().say_hello()}. {self.my_job()}"  # Приветствие с указанием кафедры

    def getMedId(self):
        return f"Мой СНИЛС - {self._med_id}"  # Метод для получения СНИЛСа

@final  # Запрещаем наследование от этого класса
class Aspirant(Student, Teacher):
    # Конструктор класса, инициализирующий имя, возраст, группу и кафедру
    def __init__(self,
                 name: str = "",
                 age: int = 0,
                 group: str = "",
                 kafedra: str = "",
                 ):
        super().__init__(name, age, group)  # Вызываем конструктор родительского класса
        self._kafedra = kafedra  # Устанавливаем кафедру

    def __del__(self):
        pass  # Метод деструктора

# Класс Admin наследуется от класса Person
class Admin(Person):
    __post = str()  # Приватное поле для хранения должности

    # Конструктор класса, инициализирующий имя, возраст и должность
    def __init__(self, name: str = "",
                 age: int = 0,
                 post: str = ""
                 ):
        super().__init__(name, age)  # Вызываем конструктор родительского класса
        self.__post = post  # Устанавливаем должность

    def __del__(self):
        pass  # Метод деструктора

    def my_post(self):
        return f"Я работаю на должности - {self.__post}"  # Метод для получения информации о должности

# Функция, принимающая объект типа Person и выводящая приветствие
def function(obj: Person):
    print(obj.say_hello())  # Выводим приветствие

# Создаем экземпляры классов
pers = Person("Христофор", 35)  # Экземпляр класса Person
stud = Student("Наташа", 25, "Py42")  # Экземпляр класса Student
admin = Admin("Мария", 29, "Директор")  # Экземпляр класса Admin
teacher = Teacher("Евгений Иванович", 65, "ДифУр")  # Экземпляр класса Teacher

# Выводим информацию о каждом объекте
print(pers)  # Вывод информации о Person
print("-=========-")
print(stud)  # Вывод информации о Student
print("-=========-")
print(teacher)  # Вывод информации о Teacher
print("-=========-")
stud.func()  # Вызываем метод, устанавливающий возраст в 0
print("-=========-")
asp = Aspirant("Степан", 26, "Py42", "МатМод")  # Экземпляр класса Aspirant
print(asp.say_hello())  # Выводим приветствие Aspirant
asp.med_id = "NewID"  # Устанавливаем новый медицинский ID
print(asp.med_id)  # Выводим медицинский ID
print("-=========-")
print(asp.getMedId())  # Выводим СНИЛС Aspirant
print("-=========-")
print(admin.say_hello())
print(admin)
print(admin.my_post())
