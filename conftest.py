import pytest

from config import TEST_VACANCIES_PATH_JSON, TEST_VACANCIES_PATH_TXT
from src.class_json import ClassJSON
from src.class_txt import ClassTXT
from src.class_vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy(
        "Менеджер по работе с клиентами",
        "https://hh.ru/vacancy/101709979",
        4_000_000,
        7_000_000,
        "Ташкент",
        "Опыт работы в продажах обязателен",
        "Консультирование клиентов",
    )


@pytest.fixture()
def vacancy2():
    return Vacancy(
        "Менеджер по работе с клиентами",
        "https://hh.ru/vacancy/101709979",
        40_000,
        70_000,
        "Ташкент",
        "Опыт работы в продажах обязателен",
        "Консультирование клиентов",
    )


@pytest.fixture()
def json_saver():
    return ClassJSON(filename=TEST_VACANCIES_PATH_JSON)


@pytest.fixture()
def txt_saver():
    return ClassTXT(filename=TEST_VACANCIES_PATH_TXT)
