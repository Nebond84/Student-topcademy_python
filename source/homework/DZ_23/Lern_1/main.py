from cars import Car

if __name__ == "__main__":
    model_name = input(f"Введите название модели: ")
    year_of_issue = int(input(f"Введите год выпуска: "))
    manufacturer = input(f"Введите производителя: ")
    engine_capacity = int(input(f"Введите мощность двигателя: "))
    color = input(f"введите цвет: ")
    price = int(input(f"Введите цену: "))

    car = Car(model_name = model_name,
              year_of_issue = year_of_issue,
              manufacturer = manufacturer,
              engine_capacity = engine_capacity,
              color = color,
              price = price)
    print(car.get_info())
    print(car.price)




