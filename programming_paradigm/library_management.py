# library_management.py

class Book:
    """A class representing a book with a title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track if the book is 
#checked out

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available (not checked out)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if it's available."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"'{title}' has been checked out.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Print all available books."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No available books.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")

