
from cars import PassengerCar,SUV,Cargo,Car,Interface


passenger_car = PassengerCar("Легковой автомобиль",
                             "Лада Granta",
                             "Седан",
                             "Черный",
                             89,
                             180,
                            890000,
                             "Механическая",
                             )



print(passenger_car)
print("=========================")
print(passenger_car.option_add("Кондиционер"))
print(passenger_car.option_add("ГУР"))
print(passenger_car.option_add("Стеклоподъемники"))
print("=========================")
print(passenger_car)
print("=========================")
print(passenger_car.options)
print("=========================")
print(passenger_car.option_remove("ГУР"))
print("=========================")
print(passenger_car)
print("=========================")
print(passenger_car.options)
print("=========================")


suv = SUV("Внедорожник",
          "Chevrolet TrailBlazer",
          "красный",
          150,
          185,
          3400000,
          "Рамный",
          "Передний привод",
          "Нет",
          "Бензин")

# print("=========================")
# print(suv)
# print("=========================")
# suv.full_drive = "Полный привод"
# print(suv.full_drive)
# print("=========================")
# print(suv.blocking_mode("Да"))
# print("=========================")
# print(suv)
# print("=========================")
# print(suv.blocking_mode("Да"))
# print("=========================")
# suv.type_full = "Дизель"
# print(suv.type_full)
# print("=========================")
# print(suv)



def drive(obj: Interface):
    print("=========================")
    print(obj.start_engine())
    print("=========================")
    print(obj.forward_moving())
    print("=========================")
    print(obj.backward_moving())
    print("=========================")
    print(obj.hand_brake())
    print("=========================")
    print("=========================")
drive(passenger_car)
# drive(suv)