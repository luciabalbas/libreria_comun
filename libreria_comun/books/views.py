from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book


# Create your views here.
class BookListView(ListView):
    """ Vista de la lista de Libros """
    model = Book
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    """ Vista detalle de un libro """
    model = Book