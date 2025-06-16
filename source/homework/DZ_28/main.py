from basement import Basement
from floor import Floor
from  roof import Roof
from additional_buildings import AdditionalBuildings


basement = Basement(120.0,4,"Свайный")
floor = Floor(85.7,4.5,4,2)
roof = Roof(90.0,1.0,"Двускатная")
buildings = AdditionalBuildings(70, 3.5)




def collect_basement():
    basement.add_commun("Газ")
    basement.add_commun("Вода")
    basement.add_commun("Канализация")
    print(basement)
    print("=====================")
    # print(basement.del_commun("Газ"))
    # print("=====================")
    # print(basement)


collect_basement()

#
def collect_floor():
  print(floor)
  print("=====================")
  total = (floor.price + basement.price)
  print(f"Общая сумма постройки = {total} р.")
  print("=====================")

collect_floor()


def collect_roof():
    print(roof)
    print("=====================")
    roof.satellite = "Да"
    print(roof)
    print("=====================")
    total = (floor.price + basement.price + roof.price)
    print(f"Общая сумма постройки = {total} р.")
    print("=====================")
    # roof.type_roof = "Конверт"
    # print(roof.type_roof)
    # print("=====================")
    # print(roof)
    # roof.satellite = "Нет"
    # print(roof)
    print("=====================")

collect_roof()

def collect_building():
    print(buildings)
    print("=====================")
    buildings.add_building("Гараж")
    print("=====================")
    print(buildings)
    print("=====================")
    total = (floor.price + basement.price + roof.price + buildings.price)
    print(f"Общая сумма всех строений = {total} р.")


collect_building()


