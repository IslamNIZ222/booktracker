# Book Tracker - Your Personal Reading Library Manager

**Author:** [Вариев Ахмед]

## 📚 Description

Book Tracker is a powerful console-based application designed to help you manage your personal reading collection. Whether you're an avid reader, a student, or someone who wants to keep track of their reading journey, this app provides all the tools you need. Track books you've read, filter by genre or page count, and never lose your reading history with persistent JSON storage.

## ✨ Features

### Core Features
- **Add Books** - Add new books with title, author, genre, and page count
- **Edit Books** - Modify existing book information
- **Delete Books** - Remove books from your collection
- **View All Books** - Display complete library with details
- **Filter by Genre** - Show books from specific genres
- **Filter by Pages** - Find books within a page range
- **Undo/Redo** - Revert or restore actions using Stack and Queue
- **JSON Storage** - Automatic save and load of all data

### Technical Features
- **MVC Architecture** - Clean separation of concerns
- **OOP Principles** - Encapsulation, inheritance, polymorphism
- **Stack & Queue** - History management with undo/redo
- **Input Validation** - Comprehensive error handling
- **Test Suite** - Full test coverage

## 🏗️ Architecture

### MVC Pattern Implementation

┌─────────────────────────────────────────────────────────────┐
│ MAIN.py │
│ (Application Entry) │
└─────────────────────────────────────────────────────────────┘
│
┌─────────────────────┼─────────────────────┐
▼ ▼ ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ MODEL │ │ VIEW │ │ CONTROLLER │
│ (book.py) │ │ (view.py) │ │(controller.py)│
├───────────────┤ ├───────────────┤ ├───────────────┤
│ - Book class │ │ - Menu display│ │ - Add book │
│ - Data model │ │ - User input │ │ - Edit book │
│ - Filtering │ │ - Output │ │ - Delete book │
│ - Storage │ │ - Messages │ │ - Filtering │
│ interface │ │ - Formatting │ │ - Undo/Redo │
└───────────────┘ └───────────────┘ └───────────────┘
│ │
▼ ▼
┌───────────────┐ ┌───────────────┐
│ STORAGE │ │ HISTORY │
│(json_storage) │ │(history_mgr) │
├───────────────┤ ├───────────────┤
│ - JSON save │ │ - Stack(LIFO) │
│ - JSON load │ │ - Queue(FIFO) │
│ - File mgmt │ │ - Undo/Redo │
└───────────────┘ └───────────────┘


### OOP Principles Applied

| Principle | Implementation | Example |
|-----------|----------------|---------|
| **Encapsulation** | Private attributes with getters/setters | `_title`, `_author`, `_pages` with property decorators |
| **Inheritance** | Not explicitly used (composition preferred) | HistoryManager uses deque for stack/queue |
| **Polymorphism** | Different filter methods | `filter_by_genre()`, `filter_by_pages()` |
| **Abstraction** | Clear separation of concerns | Model doesn't know about View |

### History Management (Stack & Queue)

Undo Stack (LIFO - Last In First Out) Redo Queue (FIFO - First In First Out)
┌─────────────┐ ┌─────────────┐
│ Action 3 │ ← Most recent │ Action 1 │ ← Oldest
├─────────────┤ ├─────────────┤
│ Action 2 │ │ Action 2 │
├─────────────┤ ├─────────────┤
│ Action 1 │ ← Oldest │ Action 3 │ ← Most recent
└─────────────┘ └─────────────┘
↓ ↓
Undo() Redo()

text

## 📁 Project Structure
book_tracker/
│
├── main.py # Application entry point
├── model/
│ ├── init.py
│ └── book.py # Book model and business logic
├── view/
│ ├── init.py
│ └── view.py # User interface and display
├── controller/
│ ├── init.py
│ └── controller.py # Command processing and logic
├── storage/
│ ├── init.py
│ └── storage.py # JSON file operations
├── utils/
│ ├── init.py
│ └── validator.py # Input validation
├── history/
│ ├── init.py
│ └── history_manager.py # Undo/Redo with Stack & Queue
├── tests/
│ ├── init.py
│ └── test_book_tracker.py # Test suite
├── data/
│ └── books.json # Persistent storage (auto-created)
├── .gitignore
└── README.md


## 🚀 Installation & Run

### Prerequisites
- Python 3.8 or higher
- Git (optional)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/book_tracker.git
cd book_tracker

Run the application

bash
python main.py
Run tests

bash
python tests/test_book_tracker.py
💻 Usage Examples
Main Menu
text
==================================================
BOOK TRACKER - Manage Your Reading Journey
==================================================
1. Add a book
2. Edit a book
3. Delete a book
4. List all books
5. Filter by genre
6. Filter by pages range
7. Undo last action
8. Redo last action
9. Save & Exit
==================================================
Example 1: Adding a Book
text
Choose option (1-9): 1

Enter book title: 1984
Enter author name: George Orwell
Enter genre: Dystopian
Enter number of pages: 328

[SUCCESS] Book '1984' added successfully!
Example 2: Listing All Books
text
Choose option (1-9): 4

All Books:
------------------------------------------------------------
  1. '1984' by George Orwell (Dystopian, 328 pages)
  2. 'To Kill a Mockingbird' by Harper Lee (Fiction, 281 pages)
  3. 'The Great Gatsby' by F. Scott Fitzgerald (Classic, 180 pages)
  4. 'Pride and Prejudice' by Jane Austen (Romance, 279 pages)
------------------------------------------------------------
  Total: 4 book(s)
Example 3: Filtering by Genre
text
Choose option (1-9): 5

Available genres: Dystopian, Fiction, Classic, Romance
Enter genre to filter: Dystopian

Books in Genre 'Dystopian':
------------------------------------------------------------
  1. '1984' by George Orwell (Dystopian, 328 pages)
------------------------------------------------------------
  Total: 1 book(s)
Example 4: Filtering by Pages Range
text
Choose option (1-9): 6

Enter minimum pages: 200
Enter maximum pages: 300

Books with 200-300 pages:
------------------------------------------------------------
  1. 'To Kill a Mockingbird' by Harper Lee (Fiction, 281 pages)
  2. 'Pride and Prejudice' by Jane Austen (Romance, 279 pages)
------------------------------------------------------------
  Total: 2 book(s)
Example 5: Editing a Book
text
Choose option (1-9): 2

All Books:
------------------------------------------------------------
  1. '1984' by George Orwell (Dystopian, 328 pages)
  2. 'To Kill a Mockingbird' by Harper Lee (Fiction, 281 pages)
------------------------------------------------------------

Enter book ID to edit: 1
Editing: 1. '1984' by George Orwell (Dystopian, 328 pages)

Enter book title: Nineteen Eighty-Four
Enter author name: George Orwell
Enter genre: Dystopian Classic
Enter number of pages: 328

[SUCCESS] Book ID 1 updated successfully!
Example 6: Deleting a Book
text
Choose option (1-9): 3

All Books:
------------------------------------------------------------
  1. '1984' by George Orwell (Dystopian, 328 pages)
  2. 'To Kill a Mockingbird' by Harper Lee (Fiction, 281 pages)
------------------------------------------------------------

Enter book ID to delete: 2

[SUCCESS] Book 'To Kill a Mockingbird' deleted successfully!
Example 7: Undo and Redo Operations
text
# Add a book
Choose option (1-9): 1
Enter book title: The Hobbit
Enter author name: J.R.R. Tolkien
Enter genre: Fantasy
Enter number of pages: 310
[SUCCESS] Book 'The Hobbit' added successfully!

# Delete a book
Choose option (1-9): 3
Enter book ID to delete: 3
[SUCCESS] Book 'The Hobbit' deleted successfully!

# Undo the deletion
Choose option (1-9): 7
[SUCCESS] Undo: Restored book 'The Hobbit'

# Redo the deletion
Choose option (1-9): 8
[SUCCESS] Redo: Re-deleted book 'The Hobbit'
Example 8: Validation Examples
Empty Title:

text
Enter book title: 
[ERROR] Title cannot be empty!
Invalid Pages:

text
Enter number of pages: -50
[ERROR] Number of pages cannot be negative!
Invalid Pages (non-numeric):

text
Enter number of pages: abc
[ERROR] Please enter a valid number!
📊 JSON Storage Format
Example of data/books.json:

json
[
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "pages": 328,
        "created_at": "2024-01-15T10:30:00.123456"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "pages": 281,
        "created_at": "2024-01-15T10:32:00.123456"
    }
]
🧪 Testing
Test Coverage
Test Category	Test Cases	Status
Book Creation	Create books with valid/invalid data	✅ Passing
Edit Operations	Modify existing books	✅ Passing
Delete Operations	Remove books from collection	✅ Passing
Filtering	By genre and pages range	✅ Passing
Validators	Empty strings, invalid numbers, boundaries	✅ Passing
History Manager	Undo/Redo with Stack and Queue	✅ Passing
Edge Cases	Empty database, non-existent IDs	✅ Passing
Serialization	JSON save/load	✅ Passing
Running Tests
bash
$ python tests/test_book_tracker.py

==================================================
RUNNING BOOK TRACKER TESTS
==================================================

Test 1: Book Creation
OK: Book creation test passed!

Test 2: Validator Tests
OK: Validator tests passed!

Test 3: Model Operations
OK: Model operations tests passed!

Test 4: History Manager (Stack & Queue)
OK: History manager tests passed!

Test 5: Edge Cases
OK: Edge cases tests passed!

==================================================
ALL TESTS PASSED SUCCESSFULLY!
==================================================
🎯 Use Cases
Personal Reading Log
Track all books you've read with titles, authors, genres, and page counts.

Reading Challenge
Filter by page count to find short or long books for reading challenges.

Genre Analysis
View all books in specific genres to analyze your reading preferences.

Gift Recommendations
Quickly find books by genre or length when recommending to friends.

🔧 Troubleshooting
Issue: JSON file not saving
Solution: Ensure the data directory exists. The application creates it automatically on first save.

Issue: Import errors in VS Code
Solution: Create all __init__.py files or configure Python path:

bash
# Create all init files
echo. > model\__init__.py
echo. > view\__init__.py
echo. > controller\__init__.py
echo. > storage\__init__.py
echo. > utils\__init__.py
echo. > history\__init__.py
echo. > tests\__init__.py
Issue: Undo not working
Note: Undo only works for actions performed in the current session. After restart, history is cleared.

Issue: Duplicate books
Note: The system allows duplicate books. You can add the same book multiple times.

🚀 Future Improvements
Add search by title/author

Implement rating system (1-5 stars)

Add reading status (Read/Reading/Want to read)

Add start and finish dates

Export library to CSV/PDF

Import from Goodreads

Add book cover images

Statistics dashboard (pages read, books per year)

Reading goals and challenges

Cloud sync

Mobile app version

GUI with tkinter or PyQt

📈 Performance
Operation	Time Complexity	Space Complexity
Add Book	O(1)	O(1)
Edit Book	O(n)	O(1)
Delete Book	O(n)	O(1)
Filter by Genre	O(n)	O(k) where k = results
Filter by Pages	O(n)	O(k) where k = results
Undo/Redo	O(1)	O(1)
Save to JSON	O(n)	O(n)
Load from JSON	O(n)	O(n)
📝 License
This project is created for educational purposes as part of a course assignment.

👤 Author
Вариев Ахмед

Course: Final Project

Date: 2026

🙏 Acknowledgments
Inspired by personal reading tracking needs

Built with Python and OOP principles

Thanks to all contributors and testers

📞 Support
For issues or questions:

Check the Troubleshooting section

Run the test suite

Ensure Python 3.8+ is installed

Verify all dependencies are present