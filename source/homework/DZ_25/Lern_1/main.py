from device import CoffeeMaker,Blender,MeatGrinder




coffee_maker = CoffeeMaker("Кофеварка"
                           ,"Polaris",
                           "красный",
                           "Germany",
                           0.7,
                           3400,
                           "да")
print(coffee_maker)
print("==================")
print(coffee_maker.device_on())
print("==================")
print(coffee_maker.make_coffee("молоко"))
print("==================")
print(coffee_maker.make_coffee())
print("==================")
print(coffee_maker.device_off())
print("==================")
print("==================")
blender = Blender("Блендер",
                  "Redmond",
                  "Черный",
                  "China",
                  0.5,
                  2100,
                  3)
print(blender)
print("==================")
print(blender.device_on())
print("==================")
print(blender.bland())
print("==================")
print(blender.bland("сливки и ягоды"))
print("==================")
print(blender.set_speed(2))
print("==================")
print(blender.bland("сливки и ягоды"))
print("==================")
print(blender.device_off())

meat_grinder = MeatGrinder("Мясорубка",
                           "Аксион",
                           "Белый",
                           "РФ",
                           1.2,
                           4700,
                           0.7)

print(meat_grinder)
print("==================")
print(meat_grinder.grind())
print("==================")
print(meat_grinder.device_on())
print("==================")
print(meat_grinder.grind())
print("==================")
print(meat_grinder.grind("Свинина",3))
print("==================")
print(meat_grinder.device_off())