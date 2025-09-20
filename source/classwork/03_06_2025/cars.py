import abc


class Interface(abc.ABC):
    def __init__(self):
        pass
    def __del__(self):
        pass

    @abc.abstractmethod
    def forward_moving(self):
        pass

    @abc.abstractmethod
    def backward_moving(self):
        pass

    @abc.abstractmethod
    def hand_brake(self):
        pass

    @abc.abstractmethod
    def start_engine(self):
        pass





class Car(Interface):
    __class_name = "Не указан"
    __name = ""
    __color = ""
    __power_engine = 0.0
    __max_speed = 0
    __price = 0



    def __init__(self,
                 class_name,
                 name,
                 color,
                 power_engine,
                 max_speed,
                 price):
        super().__init__()
        self._valid_class = ["Легковой автомобиль", "Внедорожник", "Грузовик"]

        self._car_body_types = ["Седан", "Хэтчбек", "Универсал", "Купе",
                                "Кабриолет", "Родстер", "Лифтбек", "Фаствек", "Минивэн"]

        self._transmission = ["Механическая", "Автомат", "Вариатор", "Робот"]
        self.__class_name = class_name if class_name in self._valid_class else self.__class_name
        self.__name = name
        self.__color = color
        self.__power_engine = power_engine
        self.__max_speed = max_speed
        self.__price = price


    def __del__(self):
        pass


    @property
    def class_name(self):
        return self.__class_name

    @class_name.setter
    def class_name(self,class_name):
        if class_name in self._valid_class:
            self.__class_name = class_name
        else:
            raise ValueError(f"Некорректное имя класса автомобиля!"
                             f"Требуется: Легковой автомобиль, Внедорожник, Грузовик ")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) is str:
            self.__name = name
        else:
            raise ValueError(f"Должна быть строка")

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if type(color) is str:
            self.__color = color
        else:
            raise ValueError(f"Должна быть строка")

    @property
    def power_engine(self):
        return self.__power_engine

    @power_engine.setter
    def power_engine(self, power_engine):
        if type(power_engine) is float:
            self.__power_engine = power_engine
        else:
            raise ValueError (f"Должно быть числовое значение с плавающей точкой")

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        if type(max_speed) is int:
            if max_speed > 0:
                self.__max_speed = max_speed
            else:
                raise f"Мда, не быстро она едет!!!"
        else:
            raise ValueError (f"Должно быть числовое значение")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if type(price) is int:
            if price > 0:
                self.__price = price
            else:
               raise f"Что, даром отдаем т.е. безвоздмездно? :)"
        else:
            raise ValueError (f"Должно быть числовое значение")

    @abc.abstractmethod
    def __str__(self):
        return (f"Имя класса: {self.__class_name}\n"
                f"Модель: {self.__name}\n"
                f"Цвет: {self.__color}\n"
                f"Мощность двигателя: {self.__power_engine} л,с\n"
                f"Максимальная скорость: {self.__max_speed} км/ч\n"
                f"Цена: {self.__price} р.")


class PassengerCar(Car):
    __body = None
    __transmission_box = ""


    def __init__(self,
                 class_name,
                 name,
                 body,
                 color,
                 power_engine,
                 max_speed,
                 price,
                 transmission_box,
                 ):
        super().__init__(class_name,
                         name,
                        color,
                        power_engine,
                        max_speed,
                        price)
        self.__transmission_box = transmission_box if transmission_box in self._transmission\
            else self.__transmission_box
        self.__body = body if body in self._car_body_types else self.__body
        self.__count_option = 0
        self.__options = []


    def __del__(self):
        pass

    @property
    def options(self):
        return self.__options


    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self,body):
        if body is self._car_body_types:
            self.__body = body
        else:
            raise ValueError (f"Данного кузова не существует!"
             f"Требуется: Седан,Хэтчбек,Универсал,Купе,Кабриолет,"
             f" Родстер,Лифтбек,Фаствек,Минивэн")

    @property
    def transmission_box(self):
        return self.__transmission_box

    @transmission_box.setter
    def transmission_box(self,transmission_box):
        if transmission_box in self._transmission:
            self.__transmission_box = transmission_box
        else:
            raise ValueError (f"Требуется указать: Механическая, Автомат, Вариатор, Робот")


    def option_add(self,name):
        valid_options = {"Кондиционер": 35000,
                         "ГУР": 60000,
                         "Стеклоподъемники": 45000,
                         "Мультимедиа": 30000}
        if name in valid_options:
            self.__options.append(name)
            self.__count_option += 1
            self.price += valid_options[name]
            return (f"Добавлен: {name} - стоимостью: {valid_options[name]} р.\n"
                    f"\tНовая стоимость автомобиля: {self.price} р.\n")
        else:
            return self.__count_option

    def option_remove(self, name):
        valid_options = {"Кондиционер": 35000,
                         "ГУР": 60000,
                         "Стеклоподъемники": 45000,
                         "Мультимедиа": 30000}
        if name in valid_options:
            self.__options.remove(name)
            self.__count_option -= 1
            self.price -= valid_options[name]
            return (f"Удален: {name} - стоимостью: {valid_options[name]} р.\n"
                    f"\tНовая стоимость автомобиля: {self.price} р.\n")
        else:
            return self.__count_option

    def forward_moving(self):
        return f"{super().name} едет вперед"

    def backward_moving(self):
        return f"{super().name} едет назад"

    def hand_brake(self):
        return f"{super().name} останов"

    def start_engine(self):
        return f"Двигатель запущен: Врр - Врр"


    def __str__(self):
        additional_options = self.__count_option
        return (f"{super().__str__()}\n"
                f"Тип кузова: {self.__body}\n"
                f"Коробка передач: {self.__transmission_box}\n"
                f"Кол-во дополнительных опций: {additional_options}")



class SUV(Car):
    __frame = ""
    __full_drive = ""
    __blocking = ""
    __type_full = ""
    def __init__(self,
                 class_name,
                 name,
                 color,
                 power_engine,
                 max_speed,
                 price,
                 frame,
                 full_drive,
                 blocking,
                 type_full):
        super().__init__(class_name,
                         name,
                        color,
                power_engine,
                max_speed,
                        price)
        self.__frame = frame
        self.__full_drive = full_drive
        self.__blocking = blocking
        self.__type_full = type_full

    def __del__(self):
        pass

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self,frame):
        if frame is str:
            if frame == "Рамный" or frame == "Не рамный":
                self.__frame = frame
            else:
                raise ValueError (f"Ожидается: Рамный или Не рамный")
        else:
            raise ValueError (f"Ожидается строковое значение")


    @property
    def full_drive(self):
        return self.__full_drive

    @full_drive.setter
    def full_drive(self,full_drive):
        if type(full_drive) is str:
            if (full_drive == "Передний привод"
                    or full_drive == "Задний привод"
                    or full_drive == "Полный привод"):
                self.__full_drive = full_drive
            else:
                raise ValueError (f"Ожидается: Передний привод, Задний привод, Полный привод")
        else:
            raise ValueError (f"Ожидается строка")

    @property
    def blocking(self):
        return self.__blocking

    def blocking_mode(self,blocking):
        if blocking == "Да" and self.__blocking != "Да":
            if self.__full_drive == "Полный привод":
                self.__blocking = blocking
                self.price += 300000
                return (f"Блокировка добавлена\n"
                        f" Новая стоимость авто: {self.price} р.")
            else:
                return self.__blocking
        else:
            return f"Опция уже установлена!"

    @property
    def type_full(self):
        return self.__type_full

    @type_full.setter
    def type_full(self,type_full):
        if type(type_full) is str:
            if type_full == "Бензин" or type_full == "Дизель":
                self.__type_full = type_full
            else:
                raise ValueError (f"Ожидается: Бензин или Дизель")
        else:
            raise ValueError (f"Ожидается строка")

    def forward_moving(self):
        return f"{super().name} едет вперед"

    def backward_moving(self):
        return f"{super().name} едет назад"

    def hand_brake(self):
        return f"{super().name} стоп"

    def start_engine(self):
        return f"Двигатель запущен: Врррррр"

    def __str__(self):
        return (f"{super().__str__()}\n"
                f"Рамный или нет: {self.__frame}\n"
                f"Привод: {self.__full_drive}\n"
                f"Блокировка: {self.__blocking}\n"
                f"Вид топлива: {self.__type_full}")

class Cargo(Car):
    __tonnage = 0.0
    __install_trailer = ""
    __sleep_place = ""
    __number_of_seats = 0

    def __init__(self,
                 class_name,
                 name,
                 color,
                 power_engine,
                 max_speed,
                 price,
                 tonnage,
                 install_trailer,
                 sleep_place,
                 number_of_seats):
        super().__init__(class_name,
                             name,
                             color,
                       power_engine,
                         max_speed,
                              price)
        self.__tonnage = tonnage
        self.__install_trailer = install_trailer
        self.__sleep_place = sleep_place
        self.__number_of_seats = number_of_seats

    def forward_moving(self):
        return "Двигаемся вперед"


    def backward_moving(self):
        return f"Едем назад"

    def hand_brake(self):
        return f"Стоп"

    def start_engine(self):
        return f"Двигатель запущен: Врр - Врр"


    def __str__(self):
        return (f"{super().__str__()}\n"
                f"Тоннаж: {self.__tonnage}\n"
                f"Возможность установки прицепа: {self.__install_trailer}\n"
                f"Наличие спального места {self.__sleep_place}\n"
                f"Количество мест {self.__number_of_seats}")








