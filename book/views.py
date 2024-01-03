from django.shortcuts import render, redirect
from .models import Book,Library,EBook
from django.http import HttpResponse


def book(request):
    return render(request,'home.html')

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        file_format = request.POST.get('file_format','')
        if file_format:
            new_book = Book(title=title, author=author, isbn=isbn)
            new_book.save()
            new_ebook = EBook(title=title, author=author, isbn=isbn, file_format=file_format)
            new_ebook.save()
        else:
            new_book = Book(title=title, author=author, isbn=isbn)
            new_book.save()
        return redirect('list_books')
    return render(request, 'add.html')

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list.html', {'books':books})

def search_books(request):
    result = None
    if request.method == 'POST':
        title = request.POST.get('title')
        book = Book.objects.filter(title__iexact = title).first()
        result = book.display_info() if book else "Book Is Not Available"
    return render(request, 'search.html', {'result':result})


