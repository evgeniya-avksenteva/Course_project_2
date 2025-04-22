import pytest

from src.class_vacancy import Vacancy
from src.utils import filter_vacancies, sort_vacancies


@pytest.fixture
def vacancies():
    """Создает тестовые данные для вакансий."""
    return [
        Vacancy(
            name="Python Developer",
            requirement="Experience with Python and Django",
            alternate_url="http://example.com/python-developer",
            salary_from=100000,
            salary_to=120000,
            area_name="Remote",
            responsibility="Developing applications using Python",
        ),
        Vacancy(
            name="Java Developer",
            requirement="Experience with Java and Spring",
            alternate_url="http://example.com/java-developer",
            salary_from=120000,
            salary_to=140000,
            area_name="Remote",
            responsibility="Developing applications using Java",
        ),
        Vacancy(
            name="Data Scientist",
            requirement="Experience with data analysis and Python",
            alternate_url="http://example.com/data-scientist",
            salary_from=90000,
            salary_to=110000,
            area_name="Remote",
            responsibility="Analyzing data and building models",
        ),
    ]


def test_filter_vacancies(vacancies):
    """Тестируем фильтрацию вакансий по ключевому слову."""
    filtered = filter_vacancies(vacancies, "python")
    assert len(filtered) == 2  # Должны быть 2 вакансии с "python" в названии или описании
    assert vacancies[0] in filtered
    assert vacancies[2] in filtered


def test_sort_vacancies(vacancies):
    """Тестируем сортировку вакансий по зарплате."""
    sorted_vacancies = sort_vacancies(vacancies)

    # Проверяем порядок вакансий после сортировки
    assert sorted_vacancies[0] == vacancies[1]  # Java Developer с самой высокой зарплатой
    assert sorted_vacancies[1] == vacancies[0]  # Python Developer со средней зарплатой
    assert sorted_vacancies[2] == vacancies[2]  # Data Scientist с самой низкой зарплатой
