import json
from datetime import datetime
from typing import List, Optional, Dict, Any

class Book:
    """Класс книги с инкапсуляцией"""
    
    def __init__(self, id: int, title: str, author: str, genre: str, pages: int, created_at: Optional[str] = None):
        self._id = id
        self._title = title
        self._author = author
        self._genre = genre
        self._pages = pages
        self._created_at = created_at or datetime.now().isoformat()
    
    # Геттеры и сеттеры (инкапсуляция)
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, value: str):
        self._title = value
    
    @property
    def author(self) -> str:
        return self._author
    
    @author.setter
    def author(self, value: str):
        self._author = value
    
    @property
    def genre(self) -> str:
        return self._genre
    
    @genre.setter
    def genre(self, value: str):
        self._genre = value
    
    @property
    def pages(self) -> int:
        return self._pages
    
    @pages.setter
    def pages(self, value: int):
        self._pages = value
    
    def to_dict(self) -> Dict[str, Any]:
        """Преобразование в словарь для JSON"""
        return {
            'id': self._id,
            'title': self._title,
            'author': self._author,
            'genre': self._genre,
            'pages': self._pages,
            'created_at': self._created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Book':
        """Создание книги из словаря"""
        return cls(
            id=data['id'],
            title=data['title'],
            author=data['author'],
            genre=data['genre'],
            pages=data['pages'],
            created_at=data.get('created_at')
        )
    
    def __str__(self) -> str:
        return f"{self._id}. '{self._title}' by {self._author} ({self._genre}, {self._pages} pages)"


class BookModel:
    """Модель для управления коллекцией книг"""
    
    def __init__(self):
        self._books: List[Book] = []
        self._next_id = 1
    
    def add_book(self, title: str, author: str, genre: str, pages: int) -> Book:
        """Добавление новой книги"""
        book = Book(self._next_id, title, author, genre, pages)
        self._books.append(book)
        self._next_id += 1
        return book
    
    def edit_book(self, book_id: int, title: str, author: str, genre: str, pages: int) -> bool:
        """Редактирование существующей книги"""
        book = self.get_book_by_id(book_id)
        if book:
            book.title = title
            book.author = author
            book.genre = genre
            book.pages = pages
            return True
        return False
    
    def delete_book(self, book_id: int) -> bool:
        """Удаление книги"""
        book = self.get_book_by_id(book_id)
        if book:
            self._books.remove(book)
            return True
        return False
    
    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """Получение книги по ID"""
        for book in self._books:
            if book.id == book_id:
                return book
        return None
    
    def get_all_books(self) -> List[Book]:
        """Получение всех книг"""
        return self._books.copy()
    
    def filter_by_genre(self, genre: str) -> List[Book]:
        """Фильтрация по жанру"""
        return [book for book in self._books if book.genre.lower() == genre.lower()]
    
    def filter_by_pages(self, min_pages: int, max_pages: int) -> List[Book]:
        """Фильтрация по количеству страниц"""
        return [book for book in self._books if min_pages <= book.pages <= max_pages]
    
    def get_all_genres(self) -> List[str]:
        """Получение всех уникальных жанров"""
        return list(set(book.genre for book in self._books))
    
    def load_books(self, books_data: List[Dict[str, Any]]):
        """Загрузка книг из данных"""
        self._books = [Book.from_dict(data) for data in books_data]
        if self._books:
            self._next_id = max(book.id for book in self._books) + 1
        else:
            self._next_id = 1