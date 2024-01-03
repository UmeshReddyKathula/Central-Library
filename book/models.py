from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    isbn = models.CharField(max_length = 15)

    def display_info(self):
        return(f'Title:{self.title},Author:{self.author},ISBN:{self.isbn}')
    

class EBook(Book):
    file_format = models.CharField(max_length = 10)

    def display_info(self):
        return super().display_info() + (f'File Format:{self.file_format}')
    
class Library(models.Model):
    books = models.ManyToManyField(Book)

    def add_book(self,book):
        self.books.add(book)

    def display_books(self):
        return [book.display_info() for book in self.books.all()]
    
    def search_book(self,title):
        book = self.books.filter(title__iexact = title).first()
        return book.display_info() if book else "Book Is Not Available"
