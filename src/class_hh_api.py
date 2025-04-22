import requests
from requests import Response

from src.abstract_class_api import AbstractClassAPI


class HeadHunterAPI(AbstractClassAPI):
    """Класс для подключения к hh.ru"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "per_page": "", "only_with_salary": True}

    def __get_response(self, keyword: str, per_page: int) -> Response:
        """Отправляет GET-запрос к API с заданными параметрами."""
        self.__params["text"] = keyword
        self.__params["per_page"] = per_page
        try:
            response = requests.get(self.url, headers=self.headers, params=self.__params)
            response.raise_for_status()  # Проверка на ошибки HTTP
            return response
        except requests.HTTPError as http_err:
            print(f"HTTP ошибка: {http_err} (статус код: {response.status_code})")
        except requests.ConnectionError:
            print("Ошибка соединения. Проверьте интернет-соединение.")
        except requests.Timeout:
            print("Время ожидания запроса истекло.")
        except requests.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")

        return None

    def get_response(self, keyword: str, per_page: int) -> Response:
        """Получает ответ от API по заданному ключевому слову и количеству вакансий на странице."""
        return self.__get_response(keyword, per_page)

    def get_vacancies(self, keyword: str, per_page: int):
        """Возвращает список вакансий по заданному ключевому слову."""
        response = self.get_response(keyword, per_page)
        if response is not None:
            return response.json().get("items", [])
        return []
