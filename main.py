from typing import List

from config import VACANCIES_PATH_JSON, VACANCIES_PATH_TXT
from src.class_hh_api import HeadHunterAPI
from src.class_json import ClassJSON
from src.class_txt import ClassTXT
from src.class_vacancy import Vacancy
from src.utils import display_vacancies, filter_vacancies, sort_vacancies


def main():
    """Запуск программы"""
    user_input = input(
        "Здравствуйте!\n"
        "В каком формате необходимо записать полученные данные?\n"
        "Записать в json формате - введите 1\n"
        "Записать в txt формате - введите 2\n"
        "Если необходимо удалить данные из файла - введите 3\n"
    )

    if user_input == "1":
        user_choice("json")
    elif user_input == "2":
        user_choice("txt")
    elif user_input == "3":
        user_input = input(
            "Из какого файла необходимо удалить данные?\n" "json-файл - введите 1\n" "txt-файл - введите 2\n"
        )
        if user_input == "1":
            deleter = ClassJSON(VACANCIES_PATH_JSON)
            deleter.del_data()
            print("Данные с json-файла удалены!")
        elif user_input == "2":
            deleter = ClassTXT(VACANCIES_PATH_TXT)
            deleter.del_data()
            print("Данные с txt-файла удалены!")
    return


def user_choice(file_format):
    """Функция для работы с пользователем, запись в файл выбранного формата"""

    keyword = input("Введите поисковый запрос (наименование вакансии): \n").lower()
    per_page = get_per_page_input()

    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies(keyword, per_page)

    # Преобразуем данные вакансий
    vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancies]

    # Фильтруем и сортируем вакансии
    filtered_vacancies = filter_vacancies(vacancies, keyword)
    sorted_vacancies = sort_vacancies(filtered_vacancies)

    # Выводим вакансии
    display_vacancies(sorted_vacancies)

    # Сохраняем данные в файл
    save_vacancies_to_file(sorted_vacancies, file_format)


def get_per_page_input() -> int:
    """Запрашивает у пользователя количество вакансий для вывода."""
    while True:
        user_input = input("Введите количество вакансий для вывода в топ N: \n")
        if user_input.isdigit():  # Проверяем, является ли ввод числом
            return int(user_input)  # Возвращаем корректное число
        else:
            print("Пожалуйста, введите корректное число.")  # Сообщение об ошибке


def save_vacancies_to_file(vacancies: List[Vacancy], file_format: str):
    """Сохраняет вакансии в файл выбранного формата."""

    if file_format == "json":
        vacancies_data = [vacancy.to_dict() for vacancy in vacancies]
        saver = ClassJSON(VACANCIES_PATH_JSON)
    elif file_format == "txt":
        vacancies_data = "\n".join(str(vacancy) for vacancy in vacancies)
        saver = ClassTXT(VACANCIES_PATH_TXT)
    else:
        print("Неверный формат файла.")
        return

    saver.write_data(vacancies_data)
    print("Данные записаны в файл")


if __name__ == "__main__":
    main()
