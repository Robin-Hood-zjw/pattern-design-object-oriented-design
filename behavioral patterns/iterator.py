from abc import ABC
from collections.abc import Iterator

class Book(ABC):
    def __init__(self, title: str) -> None:
        self.title = title

    def get_title(self) -> str:
        return self.title
    

class BookIterator(Iterator):
    def __init__(self, books: list[Book]) -> None:
        self.index = 0
        self.books = books

    def __next__(self) -> Book:
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration()
    
    def __iter__(self) -> Iterator:
        return self
    
class Sorted_BookIterator(Iterator):
    def __init__(self, books: list[Book]) -> None:
        self.index = 0
        self.sorted_books = sorted(books, key=lambda book: book.get_title())

    def __next__(self) -> Book:
        if self.index < len(self.sorted_books):
            book = self.sorted_books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration()
        
    def __iter__(self) -> Iterator:
        return self


class BookShelf(ABC):
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def iterator(self) -> Iterator:
        return BookIterator(self.books)
    
    def sorted_iterator(self) -> Iterator:
        return Sorted_BookIterator(self.books)
    


if __name__ == '__main__':
    bookshelf = BookShelf()
    bookshelf.add_book(Book('Book 1'))
    bookshelf.add_book(Book('Book 2'))
    bookshelf.add_book(Book('Book 3'))

    itr = bookshelf.sorted_iterator()
    for book in itr:
        print(book.get_title())
