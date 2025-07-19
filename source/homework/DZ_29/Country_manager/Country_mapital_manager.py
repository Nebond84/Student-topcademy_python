import json
import os

class CountryCapitalManager:
    def __int__(self,filename = "countries_capitals.json"):
        self.__filename = filename
        self.data = self._load_data()

    def _load_data(self):
        if os.path.exists(self.__filename):
            try:
                with open(self.__filename,"r", encoding="utf - 8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Оштбка чтения json из файла {self.__filename}. Создан пустой словарь")
                return {}
        return {}

    def _save_data(self):
        try:
            with open(self.__filename, "w", encoding="utf - 8") as f:
                json.dump(self.data, f, indent= 4,ensure_ascii= False)
            print(f"Данные успешно сохранены в {self.__filename}")
        except Exception as e:
            print(f"Ошибка при сохранении данных {e}")

