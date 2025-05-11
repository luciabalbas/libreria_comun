from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from .forms import BookForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.
class BookListView(ListView):
    """ Vista de la lista de Libros """
    model = Book
    context_object_name = 'book_list'
    paginate_by = 4
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    """ Vista detalle de un libro """
    model = Book

@method_decorator(staff_member_required, name='dispatch')
class BookCreateView(CreateView):
    """ Vista de Crear un Libro """
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:books')
    
@method_decorator(staff_member_required, name='dispatch')
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