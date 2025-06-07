class Device:
    __brand = ""
    __color = ""
    __manufacturer = ""
    __power_consumption = 0.0
    __price = 0

    def __init__(self,
                 brand = "",
                 color = "",
                 manufacturer = "",
                 power_consumption = 0.0,
                 price = 0):
        self.__brand = brand
        self.__color = color
        self.__manufacturer = manufacturer
        self.__power_consumption = power_consumption
        self.__price = price
        self.is_on = False

    def __del__(self):
        pass

    def device_on(self):
        if  not self.is_on:
            self.is_on = True
            return f"{self.__brand} - включен"
        else:
            return f"{self.__brand} - уже включен!"

    def device_off(self):
        if self.is_on:
            self.is_on = False
            return f"{self.__brand} - выключен"
        else:
            return f"{self.__brand} - уже выключен!"

    def __str__(self):
        status = "Вкл" if self.is_on else "Выкл"
        return (f"Бренд: {self.__brand}\n"
                f"Цвет: {self.__color}\n"
                f"Производитель: {self.__manufacturer}\n"
                f"Мощность потребления: {self.__power_consumption} КВт\n"
                f"Цена: {self.__price} р.\n"
                f"Состояние: {status}")

class CoffeeMaker(Device):
    __name = ""
    __cappuccino_maker = ""


    def __init__(self,name = "",
                 brand = "",
                 color = "",
                 manufacturer = "",
                 power_consumption = 0.0,
                 price = 0,
                 cappuccino_maker = ""):
        super().__init__(brand,
                 color,
                 manufacturer,
                 power_consumption,
                 price)
        self.__name = name
        self.__cappuccino_maker = cappuccino_maker


    def __del__(self):
        pass


    def make_coffee(self,milk = False):
        if self.__cappuccino_maker == "да" and self.is_on:
            if milk == "молоко":
                return f"Готовит капучино"
            else:
                return f"Готовит обычный кофе"
        elif self.__cappuccino_maker == "нет" and self.is_on:
            return (f"Капучинатор отсутствует!\n"
                    f"Готовит обычный кофе")
        else:
            return f"Сначала нужно включить устройство!"



    def __str__(self):
        return (f"Название: {self.__name}\n"
                f"{super().__str__()}\n"
                f"Капучинатор: {self.__cappuccino_maker}")



class Blender(Device):
    __name = ""
    __speed_mode = 0

    def __init__(self,
                 name="",
                 brand="",
                 color="",
                 manufacturer="",
                 power_consumption=0.0,
                 price=0,
                 speed_mode = 0):
        super().__init__(brand,
                 color,
                 manufacturer,
                 power_consumption,
                 price)
        self.__name = name
        self.__speed_mode = speed_mode
        self.current_speed = 0

    def __del__(self):
        pass


    def set_speed(self,speed):
        if 0 < speed <= self.__speed_mode:
            self.current_speed = speed
            return f"Установлена скорость {speed}"
        else:
            return f"Установите скорость от 1 до {self.__speed_mode}"


    def bland(self,ingredients = False):
        if ingredients:
            if self.is_on and self.current_speed > 0:
                return f"{self.__name} смешивает {ingredients} на скорости {self.current_speed}"
            else:
                return "Проверьте включен ли прибор и выбран ли режим скорости!"
        else:
            return f"Добавьте ингредиенты!"


    def __str__(self):
        return (f"Название: {self.__name}\n"
                f"{super().__str__()}\n"
                f"Режим скорости: {self.__speed_mode}")


class MeatGrinder(Device):
    __name = ""
    __performance = ""
    def __init__(self,
                 name="",
                 brand="",
                 color="",
                 manufacturer="",
                 power_consumption=0.0,
                 price=0,
                 performance = 0.0):
        super().__init__(brand,
                 color,
                 manufacturer,
                 power_consumption,
                 price)
        self.__name = name
        self.__performance = performance


    def __del__(self):
        pass


    def grind(self,meat_type = False,weight = False):
        if self.is_on:
            if meat_type and weight:
                return f"{self.__name} перемалывает {weight} кг. {meat_type} за {self.__performance * weight} мин."
            else:
                return f"Укажите тип и вес ингредиентов!"
        else:
            return "Попробуйте сначала включить устройство!"

    def __str__(self):
        return (f"Название: {self.__name}\n"
                f"{super().__str__()}\n"
                f"Производительность: {self.__performance} кг./мин.")



