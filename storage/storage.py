import json
import os
from typing import List, Dict

class Storage:
    """Класс для сохранения и загрузки данных в JSON"""
    
    def __init__(self, filename: str = "data/books.json"):
        self.filename = filename
        self._ensure_directory_exists()
    
    def _ensure_directory_exists(self):
        """Создание директории для файла данных, если её нет"""
        directory = os.path.dirname(self.filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
    
    def save_books(self, books: List[Dict]) -> bool:
        """Сохранение книг в JSON файл"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(books, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_books(self) -> List[Dict]:
        """Загрузка книг из JSON файла"""
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Error: Corrupted JSON file. Starting with empty database.")
            return []
        except Exception as e:
            print(f"Error loading data: {e}")
            return []