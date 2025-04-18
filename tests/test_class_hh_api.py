from unittest.mock import Mock, patch

import pytest

from src.class_hh_api import HeadHunterAPI


@pytest.fixture
def headhunter_api():
    return HeadHunterAPI()


@patch("src.class_hh_api.requests.get")
def test_get_vacancies(mock_get, headhunter_api):
    # Настройка мока для requests.get
    mock_response = Mock()
    mock_response.json.return_value = {
        "items": [
            {"name": "Python Developer", "salary": 100000},
            {"name": "Senior Python Developer", "salary": 150000},
        ]
    }
    mock_get.return_value = mock_response

    # Вызов метода get_vacancies
    keyword = "Python"
    per_page = 2
    vacancies = headhunter_api.get_vacancies(keyword, per_page)

    # Проверка, что requests.get был вызван с правильными параметрами
    mock_get.assert_called_once_with(
        headhunter_api.url, params={"text": keyword, "per_page": per_page, "only_with_salary": True}
    )

    # Проверка возвращаемых данных
    assert len(vacancies) == 2
    assert vacancies[0]["name"] == "Python Developer"
    assert vacancies[1]["name"] == "Senior Python Developer"
