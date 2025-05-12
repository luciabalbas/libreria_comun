from django.shortcuts import render, get_list_or_404
from django.views.generic.base import TemplateView
from books.models import Book

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'core/home.html'
    def get(self, request):
        last_books = get_list_or_404(Book.objects.order_by('-created')[:4])
        return render (request, 'core/home.html', {'last_books': last_books})

class SamplePageView(TemplateView):
    template_name = 'core/sample.html'