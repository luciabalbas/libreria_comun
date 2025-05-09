from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from .forms import BookForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

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
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:books')
    