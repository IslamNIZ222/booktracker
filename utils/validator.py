import re
from typing import Optional, Union

class Validator:
    """Класс для валидации ввода пользователя"""
    
    @staticmethod
    def validate_string(value: str, field_name: str) -> bool:
        """Проверка, что строка не пустая и не состоит из пробелов"""
        if not value or not value.strip():
            print(f"Error: {field_name} cannot be empty!")
            return False
        if len(value.strip()) < 2:
            print(f"Error: {field_name} must be at least 2 characters long!")
            return False
        if len(value.strip()) > 100:
            print(f"Error: {field_name} must be less than 100 characters!")
            return False
        return True
    
    @staticmethod
    def validate_pages(value: str, allow_zero: bool = False) -> Optional[int]:
        """Проверка, что количество страниц — корректное число"""
        try:
            pages = int(value)
            if pages < 0:
                print("Error: Number of pages cannot be negative!")
                return None
            if pages == 0 and not allow_zero:
                print("Error: Number of pages must be greater than 0!")
                return None
            if pages > 10000:
                print("Error: Number of pages seems too high (max 10000)!")
                return None
            return pages
        except ValueError:
            print("Error: Please enter a valid number!")
            return None
    
    @staticmethod
    def validate_id(value: str) -> Optional[int]:
        """Проверка ID книги"""
        try:
            book_id = int(value)
            if book_id <= 0:
                print("Error: ID must be a positive number!")
                return None
            return book_id
        except ValueError:
            print("Error: Please enter a valid ID!")
            return None
    
    @staticmethod
    def validate_genre(value: str) -> bool:
        """Проверка жанра"""
        valid_genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Sci-Fi', 
                       'Fantasy', 'Biography', 'History', 'Poetry', 
                       'Drama', 'Romance', 'Thriller', 'Horror']
        
        if not value or not value.strip():
            print("Error: Genre cannot be empty!")
            return False
        
        # Предлагаем подсказку, но не ограничиваем строго
        if value.strip().title() not in valid_genres:
            print(f"💡 Hint: Common genres: {', '.join(valid_genres[:5])}...")
        
        return True