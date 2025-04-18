# from src.utils import user_choice_json, user_choice_txt
from config import VACANCIES_PATH_JSON, VACANCIES_PATH_TXT
from src.abstract_class_json import AbstractClassJSON
from src.abstract_class_txt import AbstractClassTXT
from src.class_hh_api import HeadHunterAPI
from src.class_vacancy import Vacancy


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
        user_choice_json()
    elif user_input == "2":
        user_choice_txt()
    elif user_input == "3":
        user_input = input(
            "Из какого файла необходимо удалить данные?\n" "json-файл - введите 1\n" "txt-файл - введите 2\n"
        )
        if user_input == "1":
            deleter = AbstractClassJSON(VACANCIES_PATH_JSON)
            deleter.del_data()
            print("Данные с json-файла удалены!")
        elif user_input == "2":
            deleter = AbstractClassTXT(VACANCIES_PATH_TXT)
            deleter.del_data()
            print("Данные с txt-файла удалены!")
    return


def user_choice_json():
    """Функция для работы с пользователем, запись в json-файл"""

    keyword = input("Введите поисковый запрос(наименование вакансии): \n").lower()
    per_page = int(input("Введите количество вакансий для вывода в топ N: \n"))

    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies(keyword, per_page)
    vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancies]
    vacancies = sorted(vacancies, reverse=True)

    print("Топ выбранных вакансий с 'HeadHunter' по зарплате: \n")
    for i in sorted(vacancies, reverse=True):
        print(i)

    vacancies = [vacancy.to_dict() for vacancy in vacancies]
    saver = AbstractClassJSON(VACANCIES_PATH_JSON)

    saver.write_data(vacancies)
    saver.get_data()
    print("Данные записаны в json-файл")


def user_choice_txt():
    """Функция для работы с пользователем, запись в txt-файл"""

    keyword = input("Введите профессию для поиска вакансий на hh.ru: \n").lower()
    per_page = int(input("Введите количество вакансий для вывода в топ N: \n"))
    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies(keyword, per_page)
    vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancies]
    vacancies = sorted(vacancies, reverse=True)

    print("Топ выбранных вакансии с 'HeadHunter' по зарплате: \n")
    for i in sorted(vacancies, reverse=True):
        print(i)

    vacancies = "\n".join(str(vacancy) for vacancy in vacancies)
    saver = AbstractClassTXT(VACANCIES_PATH_TXT)
    saver.write_data(vacancies)
    saver.get_data()
    print("Данные записаны в txt-файл")


if __name__ == "__main__":
    main()
