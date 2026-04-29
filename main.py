#!/usr/bin/env python3
"""
Book Tracker Application
Author: [Your Name]
Description: Console application for tracking read books with MVC pattern, 
JSON storage, and undo/redo functionality
"""

from view.view import View
from controller.controller import Controller

def main():
    """Main entry point of the application"""
    print("=" * 50)
    print("WELCOME TO BOOK TRACKER")
    print("=" * 50)
    
    view = View()
    controller = Controller(view)
    
    # Load existing data
    controller.load_from_file()
    
    # Run the application
    controller.run()
    
    # Save data before exit
    if controller.save_to_file():
        print("Data saved successfully!")
    else:
        print("WARNING: Data was not saved!")

if __name__ == "__main__":
    main()