from abc import ABC, abstractmethod


class AbstractClassToFile(ABC):
    """Абстрактный класс для записи в файл"""

    def __init__(self, filename):
        self._filename = filename

    @abstractmethod
    def write_data(self, vacancies):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass
