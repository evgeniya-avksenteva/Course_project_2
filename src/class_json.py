import json

from src.abstract_class_to_file import AbstractClassToFile


class ClassJSON(AbstractClassToFile):
    """Класс для записи в json-файл"""

    def __init__(self, filename):
        """Конструктор класса"""
        self._filename = filename

    def write_data(self, vacancies):
        """Запись данных в json"""
        # Получаем существующие данные
        existing_data = self.get_data()

        # Создаем список для уникальных вакансий
        unique_vacancies = existing_data.copy()

        # Добавляем новые вакансии только если их нет в списке
        for new_vacancy in vacancies:
            if new_vacancy not in unique_vacancies:
                unique_vacancies.append(new_vacancy)

        # Записываем обратно в файл
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump(unique_vacancies, file, ensure_ascii=False, indent=4)

    def get_data(self):
        """Получение данных json"""
        try:
            with open(self._filename, encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def del_data(self):
        """Удаление данных из файла"""
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
