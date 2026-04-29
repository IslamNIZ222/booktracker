from typing import List, Tuple, Optional
from model.book import Book

class View:
    """Класс для отображения данных и взаимодействия с пользователем"""
    
    @staticmethod
    def display_menu():
        """Отображение главного меню"""
        print("\n" + "="*50)
        print("BOOK TRACKER - Manage Your Reading Journey")
        print("="*50)
        print("1. Add a book")
        print("2. Edit a book")
        print("3. Delete a book")
        print("4. List all books")
        print("5. Filter by genre")
        print("6. Filter by pages range")
        print("7. Undo last action")
        print("8. Redo last action")
        print("9. Save & Exit")
        print("="*50)
    
    @staticmethod
    def get_input(prompt: str) -> str:
        """Получение ввода от пользователя"""
        return input(prompt).strip()
    
    @staticmethod
    def display_books(books: List[Book], title: str = "Books List"):
        """Отображение списка книг"""
        if not books:
            print("\nNo books found!")
            return
        
        print(f"\n{title}:")
        print("-" * 60)
        for book in books:
            print(f"  {book}")
        print("-" * 60)
        print(f"  Total: {len(books)} book(s)")
    
    @staticmethod
    def display_message(message: str, is_error: bool = False):
        """Отображение сообщения"""
        prefix = "ERROR:" if is_error else "SUCCESS:"
        print(f"\n{prefix} {message}")
    
    @staticmethod
    def get_book_details() -> Tuple[str, str, str, int]:
        """Получение деталей книги от пользователя с валидацией"""
        from utils.validator import Validator
        
        while True:
            title = View.get_input("Enter book title: ")
            if Validator.validate_string(title, "Title"):
                break
        
        while True:
            author = View.get_input("Enter author name: ")
            if Validator.validate_string(author, "Author"):
                break
        
        while True:
            genre = View.get_input("Enter genre (Fiction, Mystery, Sci-Fi, etc.): ")
            if Validator.validate_string(genre, "Genre"):
                break
        
        while True:
            pages_str = View.get_input("Enter number of pages: ")
            pages = Validator.validate_pages(pages_str)
            if pages is not None:
                break
        
        return title, author, genre, pages
    
    @staticmethod
    def get_book_id(action: str) -> int:
        """Получение ID книги от пользователя"""
        from utils.validator import Validator
        
        while True:
            id_str = View.get_input(f"Enter book ID to {action}: ")
            book_id = Validator.validate_id(id_str)
            if book_id is not None:
                return book_id
    
    @staticmethod
    def get_filter_genre() -> str:
        """Получение жанра для фильтрации"""
        return View.get_input("Enter genre to filter: ")
    
    @staticmethod
    def get_filter_pages_range() -> Tuple[int, int]:
        """Получение диапазона страниц для фильтрации"""
        from utils.validator import Validator
        
        while True:
            min_str = View.get_input("Enter minimum pages: ")
            min_pages = Validator.validate_pages(min_str, allow_zero=True)
            if min_pages is not None:
                break
        
        while True:
            max_str = View.get_input("Enter maximum pages: ")
            max_pages = Validator.validate_pages(max_str, allow_zero=True)
            if max_pages is not None:
                break
        
        return min_pages, max_pages
    
    @staticmethod
    def display_error(message: str):
        """Отображение ошибки"""
        print(f"\n[ERROR] {message}")
    
    @staticmethod
    def display_success(message: str):
        """Отображение успешного сообщения"""
        print(f"\n[SUCCESS] {message}")