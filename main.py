from config import VACANCIES_PATH_TXT, VACANCIES_PATH_JSON
from src.abstract_class_json import AbstractClassJSON
from src.abstract_class_txt import AbstractClassTXT
from src.utils import user_choice_json, user_choice_txt


def main():
    """ Запуск программы """
    user_input = input("Здравствуйте!\n"
                       "В каком формате необходимо записать полученные данные?\n"
                       "Записать в json формате - введите 1\n"
                       "Записать в txt формате - введите 2\n"
                       "Если необходимо удалить данные из файла - введите 3\n")

    if user_input == "1":
        user_choice_json()
    elif user_input == "2":
        user_choice_txt()
    elif user_input == "3":
        user_input = input("Из какого файла необходимо удалить данные?\n"
                           "json-файл - введите 1\n"
                           "txt-файл - введите 2\n")
        if user_input == "1":
            deleter = AbstractClassJSON(VACANCIES_PATH_JSON)
            deleter.del_data()
            print("Данные с json-файла удалены!")
        elif user_input == "2":
            deleter = AbstractClassTXT(VACANCIES_PATH_TXT)
            deleter.del_data()
            print("Данные с txt-файла удалены!")
    return


if __name__ == "__main__":
    main()