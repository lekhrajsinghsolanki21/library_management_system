import json
import os

BOOKS_FILE = "books.json"

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

class Library:
    def __init__(self, filename=BOOKS_FILE):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return [Book(**data) for data in json.load(f)]
        return []

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_books()
        print("Book added successfully!")

    def list_books(self):
        if not self.books:
            print("No books available.")
            return
        for b in self.books:
            status = "Available" if b.available else "Borrowed"
            print(f"{b.title} by {b.author} (ISBN: {b.isbn}) - {status}")

    def borrow_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn and b.available:
                b.available = False
                self.save_books()
                print("Book borrowed successfully!")
                return
        print("Book not available.")

    def return_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn and not b.available:
                b.available = True
                self.save_books()
                print("Book returned successfully!")
                return
        print("Invalid return request.")

def library_menu():
    lib = Library()
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            lib.add_book(title, author, isbn)
        elif choice == "2":
            lib.list_books()
        elif choice == "3":
            isbn = input("Enter ISBN to borrow: ")
            lib.borrow_book(isbn)
        elif choice == "4":
            isbn = input("Enter ISBN to return: ")
            lib.return_book(isbn)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    library_menu()
