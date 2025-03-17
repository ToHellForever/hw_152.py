"""
В данном задании вам предстоит создать классы для работы с различными типами файлов: JSON, TXT и CSV. Вы также создадите абстрактный класс, который будет предписывать методы для чтения, записи и добавления данных в файлы. Ваша задача — реализовать наследование и полиморфизм в Python с использованием библиотеки ABC.
"""

from abc import ABC, abstractmethod
from typing import *
import json
import csv


class AbstractFile(ABC):
    """
    Абстрактный класс для работы с файлами.
    """
    def __init__(self, file_path: str) -> None:
        """
        Инициализирует объект с указанным путём к файлу."""
        self.file_path = file_path

    @abstractmethod
    def read(self) -> Any:
        """
        Читает данные из файла.
        """
        pass

    @abstractmethod
    def write(self, data: Any) -> None:
        """
        Записывает данные в файл.
        """
        pass

    @abstractmethod
    def append(self, data: Any) -> None:
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
                file_content: list[str] = [strong.strip() for strong in file.readlines()]
                return file_content
            
        except FileNotFoundError:
            print("Файл не найден")
            return []


    def write(self, data: list[str]) -> None:
        """
        Записывает строки в текстовый файл, разделяя их переводами строк.
        """
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                write_data: str = "\n".join(data)
                file.write(write_data)
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")
            raise

    def append(self, data: list[str]) -> None:
        """
        Добавляет строки в конец текстового файла, разделяя их переводами строк.
        """
        try:
            with open(self.file_path, "a", encoding="utf-8") as file:
                write_data: str = "\n".join(data)
                file.write("\n" + write_data)
        except Exception as e:
            print(f"Ошибка при добавлении в файл: {e}")
            raise
            
            
class JsonFile(AbstractFile):
    """
    Класс для работы с файлами в формате JSON.
    """
    def read(self) -> dict:
        """
        Читает данные из JSON-файла и возвращает словарь.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data: Dict = json.load(file)
                return data
            if not data:
                return {}
        except FileNotFoundError:
            print("Файл не найден")
            return {}
        
    def write(self, data: Union[dict, list]) -> None:
        """
        Записывает данные в JSON-файл.
        """
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")
            
    def append(self, data: dict) -> None:
        """
        Добавляет данные в конец JSON-файла.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                existing_data: dict = json.load(file)
            existing_data.update(data)
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при добавлении в файл: {e}")
        
        
        
class CsvFile(AbstractFile):
    """
    Класс для работы с файлами в формате CSV.
    """
    def read(self) -> list[dict]:
        """
        Читает данные из CSV-файла и возвращает список словарей.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            print("Файл не найден")
            return []
        
    def write(self, data: list[dict]) -> None:
        """
        Записывает данные в CSV-файл.
        """
        try:
            with open(self.file_path, "w", encoding="utf-8", newline="") as file:
                if not data:
                    return 
                fieldnames: List[str] = data[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")
            
    def append(self, data: list[dict]) -> None:
            """
            Добавляет данные в конец CSV-файла.
            """
            try:
                with open(self.file_path, "a", encoding="utf-8", newline="") as file:
                    fieldnames = data[0].keys()
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writerows(data)
            except Exception as e:
                print(f"Ошибка при добавлении в файл: {e}")
