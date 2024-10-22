# library.py

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __repr__(self):
        return f"<Book({self.book_id}, {self.title}, {self.author})>"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Ajoute un livre à la bibliothèque."""
        self.books.append(book)

    def remove_book(self, book_id):
        """Supprime un livre de la bibliothèque en fonction de son ID."""
        self.books = [book for book in self.books if book.book_id != book_id]

    def find_book(self, book_id):
        """Recherche un livre par son ID."""
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def list_books(self):
        """Retourne la liste de tous les livres dans la bibliothèque."""
        return self.books
