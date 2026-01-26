from relationship_app.models import Author, Book, Library, Librarian


# Query 1: All books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(books_by_author)


# Query 2: List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
library_books = library.books.all()
print(library_books)


# Query 3: Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(librarian)
