from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .models import Book


# Create your views here.
def index(request):
    books  = Book.objects.all()
    no_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "no_books": no_books,
        "avg_rating": avg_rating
    })
def book_detail(require, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(require, "book_outlet/book_detail.html", {
        "book": book
    })