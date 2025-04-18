class Vacancy:
    """Класс для работы с вакансиями"""

    # __slots__ = ("name", "alternate_url", "salary_from", "salary_to", "area_name", "requirement", "responsibility")

    # def __init__(self, name, alternate_url, salary_from, salary_to, area_name, requirement, responsibility):
    #     """Конструктор класса"""
    #
    #     self.name: str = name
    #     self.alternate_url: str = alternate_url
    #     self.salary_from: int = salary_from
    #     self.salary_to: int = salary_to
    #     self.area_name: str = area_name
    #     self.requirement: str = requirement
    #     self.responsibility: str = responsibility
    #
    # def __str__(self) -> str:
    #     """Строковое представление вакансии"""
    #
    #     return (
    #         f"Наименование вакансии: {self.name}\n"
    #         f"Ссылка на вакансию: {self.alternate_url}\n"
    #         f"Зарплата: от {self.salary_from} до {self.salary_to}\n"
    #         f"Место работы: {self.area_name}\n"
    #         f"Краткое описание: {self.requirement}\n"
    #         f"{self.responsibility}\n"
    #     )
    #
    # def __lt__(self, other) -> bool:
    #     """Метод сравнения от большего к меньшему"""
    #
    #     return self.salary_from < other.salary_from
    #
    # @classmethod
    # def from_hh_dict(cls, vacancy_data: dict):
    #     """Метод возвращает экземпляр класса в виде списка"""
    #
    #     salary = vacancy_data.get("salary")
    #
    #     return cls(
    #         vacancy_data["name"],
    #         vacancy_data["alternate_url"],
    #         salary.get("from") if salary.get("from") else 0,
    #         salary.get("to") if salary.get("to") else 0,
    #         vacancy_data["area"]["name"],
    #         vacancy_data["snippet"]["requirement"],
    #         vacancy_data["snippet"]["responsibility"],
    #     )
    #
    # def to_dict(self) -> dict:
    #     """Метод возвращает вакансию в виде словаря"""
    #
    #     return {
    #         "name": self.name,
    #         "alternate_url": self.alternate_url,
    #         "salary_from": self.salary_from,
    #         "salary_to": self.salary_to,
    #         "area_name": self.area_name,
    #         "requirement": self.requirement,
    #         "responsibility": self.responsibility,
    #     }

    __slots__ = ("name", "alternate_url", "salary_from", "salary_to", "area_name", "requirement", "responsibility")

    def __init__(
        self,
        name: str,
        alternate_url: str,
        salary_from: int,
        salary_to: int,
        area_name: str,
        requirement: str,
        responsibility: str,
    ):
        """Конструктор класса"""

        self.name = self._validate_name(name)
        self.alternate_url = self._validate_url(alternate_url)
        self.salary_from = self._validate_salary(salary_from)
        self.salary_to = self._validate_salary(salary_to)
        self.area_name = area_name  # Можно добавить валидацию для area_name
        self.requirement = requirement  # Можно добавить валидацию для requirement
        self.responsibility = responsibility  # Можно добавить валидацию для responsibility

    def _validate_name(self, name: str) -> str:
        """Проверка корректности названия вакансии"""
        if not isinstance(name, str) or not name:
            raise ValueError("Название вакансии должно быть непустой строкой")
        return name

    def _validate_url(self, url: str) -> str:
        """Проверка корректности URL вакансии"""
        if not isinstance(url, str) or not url.startswith("http"):
            raise ValueError("Ссылка на вакансию должна быть корректным URL")
        return url

    def _validate_salary(self, salary: int) -> int:
        """Проверка корректности зарплаты"""
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Зарплата должна быть неотрицательным числом")
        return salary

    def __str__(self) -> str:
        """Строковое представление вакансии"""

        return (
            f"Наименование вакансии: {self.name}\n"
            f"Ссылка на вакансию: {self.alternate_url}\n"
            f"Зарплата: от {self.salary_from} до {self.salary_to}\n"
            f"Место работы: {self.area_name}\n"
            f"Краткое описание: {self.requirement}\n"
            f"{self.responsibility}\n"
        )

    def __lt__(self, other) -> bool:
        """Метод сравнения от большего к меньшему"""

        return self.salary_from < other.salary_from

    @classmethod
    def from_hh_dict(cls, vacancy_data: dict):
        """Метод возвращает экземпляр класса из словаря"""

        salary = vacancy_data.get("salary")

        return cls(
            vacancy_data["name"],
            vacancy_data["alternate_url"],
            salary.get("from") if salary.get("from") else 0,
            salary.get("to") if salary.get("to") else 0,
            vacancy_data["area"]["name"],
            vacancy_data["snippet"]["requirement"],
            vacancy_data["snippet"]["responsibility"],
        )

    def to_dict(self) -> dict:
        """Метод возвращает вакансию в виде словаря"""

        return {
            "name": self.name,
            "alternate_url": self.alternate_url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "area_name": self.area_name,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
        }
