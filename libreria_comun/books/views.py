from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book, Genre
from .forms import BookForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
class BookListView(ListView):
    """ Vista de la lista de Libros """
    model = Book
    context_object_name = 'book_list'
    paginate_by = 4
    template_name = 'books/book_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        # Add in the reports list to context
        context['genre_list'] = Genre.objects.all()
        return context

class BookDetailView(DetailView):
    """ Vista detalle de un libro """
    model = Book

@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    """ Vista de Crear un Libro """
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:books')
    
@method_decorator(login_required, name='dispatch')
class BookUpdate(UpdateView):
    """ Vista de Editar un Libro """
    model = Book
    form_class = BookForm
    template_name_suffix='_update_form'
    def get_success_url(self):
        return reverse_lazy('books:update', args=[self.object.id]) + '?ok'
    
@method_decorator(staff_member_required, name='dispatch')
class BookDelete(DeleteView):
    """ Vista de Eliminar un Libro """
    model = Book
    success_url = reverse_lazy('books:books')

def search_book(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', None)
        books = Book.objects.filter(title__contains=searched)
        return render(request, 'books/search_book.html', {'searched': searched, 'books': books})
    else:
        return render(request, 'books/search_book.html', {})

class GenreList(ListView):
    model = Book
    def get(self, request, genre_id):
        genre_list = get_list_or_404(Genre)
        genre = get_object_or_404(Genre, id=genre_id)
        books = get_list_or_404(Book, genres=genre)
        return render(request, 'books/genre_list.html', {'genre': genre, 'book_list': books, 'genre_list': genre_list})