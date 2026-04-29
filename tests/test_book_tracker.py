#!/usr/bin/env python3
"""
Test suite for Book Tracker application
Tests positive, negative, and edge cases
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.book import BookModel, Book
from utils.validator import Validator
from history.history_manager import HistoryManager

def test_book_creation():
    """Тест создания книги"""
    print("\nTest 1: Book Creation")
    book = Book(1, "1984", "George Orwell", "Dystopian", 328)
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.genre == "Dystopian"
    assert book.pages == 328
    print("OK: Book creation test passed!")

def test_validator():
    """Тест валидации"""
    print("\nTest 2: Validator Tests")
    
    # Positive cases
    assert Validator.validate_string("Valid Title", "Title") == True
    assert Validator.validate_pages("100") == 100
    assert Validator.validate_pages("0", allow_zero=True) == 0
    
    # Negative cases
    assert Validator.validate_string("", "Title") == False
    assert Validator.validate_string("A", "Title") == False
    assert Validator.validate_pages("-5") == None
    assert Validator.validate_pages("abc") == None
    assert Validator.validate_pages("100000") == None  # Too many pages
    
    print("OK: Validator tests passed!")

def test_model_operations():
    """Тест операций модели"""
    print("\nTest 3: Model Operations")
    model = BookModel()
    
    # Add books
    book1 = model.add_book("Test Book", "Test Author", "Fiction", 200)
    book2 = model.add_book("Another Book", "Another Author", "Mystery", 350)
    
    assert len(model.get_all_books()) == 2
    
    # Filter by genre
    fiction_books = model.filter_by_genre("Fiction")
    assert len(fiction_books) == 1
    
    # Filter by pages
    pages_range = model.filter_by_pages(100, 300)
    assert len(pages_range) == 1
    
    # Edit book
    model.edit_book(book1.id, "Updated Title", "Updated Author", "Sci-Fi", 500)
    updated = model.get_book_by_id(book1.id)
    assert updated.title == "Updated Title"
    
    # Delete book
    model.delete_book(book1.id)
    assert len(model.get_all_books()) == 1
    
    print("OK: Model operations tests passed!")

def test_history_manager():
    """Тест истории (стек и очередь)"""
    print("\nTest 4: History Manager (Stack & Queue)")
    history = HistoryManager()
    
    # Push actions
    history.push_action({'type': 'ADD', 'data': 'Book 1'})
    history.push_action({'type': 'ADD', 'data': 'Book 2'})
    history.push_action({'type': 'DELETE', 'data': 'Book 1'})
    
    assert history.can_undo() == True
    
    # Undo (stack - LIFO)
    last_action = history.undo()
    assert last_action['type'] == 'DELETE'
    
    # Redo (queue - FIFO behavior for redo)
    assert history.can_redo() == True
    redone_action = history.redo()
    assert redone_action['type'] == 'DELETE'
    
    print("OK: History manager tests passed!")

def test_edge_cases():
    """Тест граничных случаев"""
    print("\nTest 5: Edge Cases")
    model = BookModel()
    
    # Empty database
    assert len(model.get_all_books()) == 0
    
    # Delete non-existent book
    assert model.delete_book(999) == False
    
    # Edit non-existent book
    assert model.edit_book(999, "Title", "Author", "Genre", 100) == False
    
    # Filter empty database
    assert len(model.filter_by_genre("Fiction")) == 0
    assert len(model.filter_by_pages(1, 1000)) == 0
    
    # Book with minimum valid values
    book = model.add_book("AB", "AB", "Fiction", 1)
    assert book.pages == 1
    
    print("OK: Edge cases tests passed!")

def run_all_tests():
    """Запуск всех тестов"""
    print("\n" + "="*50)
    print("RUNNING BOOK TRACKER TESTS")
    print("="*50)
    
    try:
        test_book_creation()
        test_validator()
        test_model_operations()
        test_history_manager()
        test_edge_cases()
        
        print("\n" + "="*50)
        print("ALL TESTS PASSED SUCCESSFULLY!")
        print("="*50)
        return True
    except AssertionError as e:
        print(f"\nTest failed: {e}")
        return False
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        return False

if __name__ == "__main__":
    run_all_tests()