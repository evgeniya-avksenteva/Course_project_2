from typing import List

from src.class_vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], keyword: str) -> List[Vacancy]:
    """Фильтрует вакансии по ключевому слову в названии или описании."""
    return [
        vacancy for vacancy in vacancies if keyword in vacancy.name.lower() or keyword in vacancy.requirement.lower()
    ]


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортирует вакансии по зарплате от большего к меньшему."""
    return sorted(vacancies, reverse=True)


def display_vacancies(vacancies: List[Vacancy]) -> None:
    """Выводит список вакансий на экран."""
    print("Топ выбранных вакансий с 'HeadHunter' по зарплате: \n")
    for vacancy in vacancies:
        print(vacancy)
