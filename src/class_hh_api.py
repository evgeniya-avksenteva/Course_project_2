import requests
from requests import Response

from src.abstract_class_api import AbstractClassAPI


class HeadHunterAPI(AbstractClassAPI):
    """Класс для подключения к hh.ru"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "per_page": "", "only_with_salary": True}

    def __get_response(self, keyword, per_page) -> Response:
        self.__params["text"] = keyword
        self.__params["per_page"] = per_page
        return requests.get(self.url, params=self.__params)

    def get_response(self, keyword: str, per_page: int) -> Response:
        return self.__get_response(keyword, per_page)

    def get_vacancies(self, keyword: str, per_page: int):
        return self.get_response(keyword, per_page).json()["items"]
