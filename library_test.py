# test_library.py
import pytest
from Library import Book, Library

@pytest.fixture
def library():
    """Fixture qui initialise une bibliothèque pour chaque test."""
    return Library()

def test_add_book(library):
    """Test l'ajout d'un livre."""
    book = Book(1, "1984", "George Orwell")
    library.add_book(book)
    assert len(library.list_books()) == 1
    assert library.list_books()[0].title == "1984"

def test_remove_book(library):
    """Test la suppression d'un livre."""
    book1 = Book(1, "1984", "George Orwell")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")
    library.add_book(book1)
    library.add_book(book2)
    library.remove_book(1)
    assert len(library.list_books()) == 1
    assert library.list_books()[0].book_id == 2

def test_find_book(library):
    """Test la recherche d'un livre par ID."""
    book = Book(1, "1984", "George Orwell")
    library.add_book(book)
    found_book = library.find_book(1)
    assert found_book is not None
    assert found_book.title == "1984"

def test_find_book_not_found(library):
    """Test la recherche d'un livre inexistant."""
    found_book = library.find_book(99)
    assert found_book is None

def test_list_books(library):
    """Test le listing des livres."""
    book1 = Book(1, "1984", "George Orwell")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")
    library.add_book(book1)
    library.add_book(book2)
    books = library.list_books()
    assert len(books) == 2
    assert books[0].title == "1984"
    assert books[1].title == "To Kill a Mockingbird"
