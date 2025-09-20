from basement import Basement
from floor import Floor


basement = Basement(60.0,4,"Свайный")
floor = Floor(55.7,4.5,4,2)



def collect_basement():
    basement.add_commun("Газ")
    basement.add_commun("Вода")
    basement.add_commun("Канализация")
    print(basement)
    print("=====================")
collect_basement()

#
def collect_floor():
  print(floor)
  print("=====================")
  total = floor + basement
  print(f"Общая сумма постройки = {total} р.")
  print("=====================")

collect_floor()

# total = (floor.price + basement.price)
# print(f"Общая сумма постройки = {total} р.")
# total = floor + basement
# print(f"Общая сумма постройки = {total} р.")


