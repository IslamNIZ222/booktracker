from model.book import BookModel
from view.view import View
from storage.storage import Storage
from history.history_manager import HistoryManager, ActionType

class Controller:
    """Контроллер для обработки команд пользователя"""
    
    def __init__(self, view: View):
        self.model = BookModel()
        self.view = view
        self.storage = Storage()
        self.history = HistoryManager()
    
    def run(self):
        """Главный цикл приложения"""
        while True:
            self.view.display_menu()
            choice = self.view.get_input("Choose option (1-9): ")
            
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.edit_book()
            elif choice == '3':
                self.delete_book()
            elif choice == '4':
                self.list_books()
            elif choice == '5':
                self.filter_by_genre()
            elif choice == '6':
                self.filter_by_pages()
            elif choice == '7':
                self.undo_action()
            elif choice == '8':
                self.redo_action()
            elif choice == '9':
                self.view.display_message("Goodbye!")
                break
            else:
                self.view.display_error("Invalid choice! Please select 1-9.")
    
    def add_book(self):
        """Добавление новой книги"""
        title, author, genre, pages = self.view.get_book_details()
        
        # Сохраняем действие для отмены
        book = self.model.add_book(title, author, genre, pages)
        self.history.push_action({
            'type': ActionType.ADD,
            'book': book.to_dict()
        })
        
        self.view.display_success(f"Book '{title}' added successfully!")
    
    def edit_book(self):
        """Редактирование книги"""
        books = self.model.get_all_books()
        if not books:
            self.view.display_error("No books to edit!")
            return
        
        self.view.display_books(books)
        book_id = self.view.get_book_id("edit")
        
        book = self.model.get_book_by_id(book_id)
        if not book:
            self.view.display_error(f"Book with ID {book_id} not found!")
            return
        
        # Сохраняем старые данные для отмены
        old_data = book.to_dict()
        
        self.view.display_message(f"Editing: {book}")
        title, author, genre, pages = self.view.get_book_details()
        
        if self.model.edit_book(book_id, title, author, genre, pages):
            self.history.push_action({
                'type': ActionType.EDIT,
                'book_id': book_id,
                'old_data': old_data,
                'new_data': {'title': title, 'author': author, 'genre': genre, 'pages': pages}
            })
            self.view.display_success(f"Book ID {book_id} updated successfully!")
        else:
            self.view.display_error("Failed to update book!")
    
    def delete_book(self):
        """Удаление книги"""
        books = self.model.get_all_books()
        if not books:
            self.view.display_error("No books to delete!")
            return
        
        self.view.display_books(books)
        book_id = self.view.get_book_id("delete")
        
        book = self.model.get_book_by_id(book_id)
        if not book:
            self.view.display_error(f"Book with ID {book_id} not found!")
            return
        
        # Сохраняем книгу для возможной отмены
        deleted_book = book.to_dict()
        
        if self.model.delete_book(book_id):
            self.history.push_action({
                'type': ActionType.DELETE,
                'book': deleted_book
            })
            self.view.display_success(f"Book '{deleted_book['title']}' deleted successfully!")
        else:
            self.view.display_error("Failed to delete book!")
    
    def list_books(self):
        """Отображение всех книг"""
        books = self.model.get_all_books()
        if books:
            self.view.display_books(books, "All Books")
        else:
            self.view.display_message("No books in the library yet. Add some!")
    
    def filter_by_genre(self):
        """Фильтрация книг по жанру"""
        genres = self.model.get_all_genres()
        if genres:
            self.view.display_message(f"Available genres: {', '.join(genres)}")
        
        genre = self.view.get_filter_genre()
        filtered_books = self.model.filter_by_genre(genre)
        
        if filtered_books:
            self.view.display_books(filtered_books, f"Books in Genre '{genre}'")
        else:
            self.view.display_message(f"No books found in genre '{genre}'")
    
    def filter_by_pages(self):
        """Фильтрация книг по диапазону страниц"""
        min_pages, max_pages = self.view.get_filter_pages_range()
        
        if min_pages > max_pages:
            self.view.display_error("Minimum pages cannot be greater than maximum pages!")
            return
        
        filtered_books = self.model.filter_by_pages(min_pages, max_pages)
        
        if filtered_books:
            self.view.display_books(filtered_books, f"Books with {min_pages}-{max_pages} pages")
        else:
            self.view.display_message(f"No books found with {min_pages}-{max_pages} pages")
    
    def undo_action(self):
        """Отмена последнего действия (стек)"""
        if not self.history.can_undo():
            self.view.display_error("Nothing to undo!")
            return
        
        action = self.history.undo()
        if not action:
            return
        
        if action['type'] == ActionType.ADD:
            # Отмена добавления: удаляем книгу
            book_id = action['book']['id']
            self.model.delete_book(book_id)
            self.view.display_success(f"Undo: Removed book '{action['book']['title']}'")
        
        elif action['type'] == ActionType.EDIT:
            # Отмена редактирования: восстанавливаем старые данные
            book_id = action['book_id']
            old = action['old_data']
            self.model.edit_book(book_id, old['title'], old['author'], old['genre'], old['pages'])
            self.view.display_success(f"Undo: Restored book '{old['title']}'")
        
        elif action['type'] == ActionType.DELETE:
            # Отмена удаления: добавляем книгу обратно
            book_data = action['book']
            self.model.add_book(book_data['title'], book_data['author'], 
                              book_data['genre'], book_data['pages'])
            self.view.display_success(f"Undo: Restored book '{book_data['title']}'")
    
    def redo_action(self):
        """Повтор отменённого действия (очередь)"""
        if not self.history.can_redo():
            self.view.display_error("Nothing to redo!")
            return
        
        action = self.history.redo()
        if not action:
            return
        
        if action['type'] == ActionType.ADD:
            book_data = action['book']
            self.model.add_book(book_data['title'], book_data['author'], 
                              book_data['genre'], book_data['pages'])
            self.view.display_success(f"Redo: Re-added book '{book_data['title']}'")
        
        elif action['type'] == ActionType.EDIT:
            book_id = action['book_id']
            new = action['new_data']
            self.model.edit_book(book_id, new['title'], new['author'], new['genre'], new['pages'])
            self.view.display_success(f"Redo: Re-applied edit to book ID {book_id}")
        
        elif action['type'] == ActionType.DELETE:
            book_data = action['book']
            self.model.delete_book(book_data['id'])
            self.view.display_success(f"Redo: Re-deleted book '{book_data['title']}'")
    
    def save_to_file(self) -> bool:
        """Сохранение данных в JSON"""
        books_data = [book.to_dict() for book in self.model.get_all_books()]
        return self.storage.save_books(books_data)
    
    def load_from_file(self):
        """Загрузка данных из JSON"""
        books_data = self.storage.load_books()
        if books_data:
            self.model.load_books(books_data)
            self.view.display_success(f"Loaded {len(books_data)} books from storage")