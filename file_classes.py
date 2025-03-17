"""
В данном задании вам предстоит создать классы для работы с различными типами файлов: JSON, TXT и CSV. Вы также создадите абстрактный класс, который будет предписывать методы для чтения, записи и добавления данных в файлы. Ваша задача — реализовать наследование и полиморфизм в Python с использованием библиотеки ABC.
"""

from abc import ABC, abstractmethod


class AbstractFile(ABC):
    """
    Абстрактный класс для работы с файлами.
    """
    def __init__(self, file_path: str) -> None:
        """
        Инициализирует объект с указанным путём к файлу."""
        self.file_path = file_path

    @abstractmethod
    def read(self):
        """
        Читает данные из файла.
        """
        pass

    @abstractmethod
    def write(self, data):
        """
        Записывает данные в файл.
        """
        pass

    @abstractmethod
    def append(self, data):
        """
        Добавляет данные в конец файла.
        """
        pass


class TxtFile(AbstractFile):
    """
    Класс для работы с текстовыми файлами.
    """
    def read(self) -> list[str]:
        """
        Читает данные из текстового файла и возвращает список строк.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                clear_data = [strong.strip() for strong in file.readlines()]
                return clear_data
            
        except FileNotFoundError:
            print("Файл не найден")
            return []


    def write(self, *data: str) -> None:
        """
        Записывает строки в текстовый файл, разделяя их переводами строк.
        """
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                write_data = "\n".join(data)
                file.write(write_data)
        except Exception as e:
            print("Ошибка при записи в файл: {e}")


    def append(self, *data: str) -> None:
        """
        Добавляет строки в конец текстового файла, разделяя их переводами строк.
        """
        try:
            with open(self.file_path, "a", encoding="utf-8") as file:
                write_data = "\n".join(data)
                file.write("\n" + write_data)
        except Exception as e:
            print(f"Ошибка при добавлении в файл: {e}")
            