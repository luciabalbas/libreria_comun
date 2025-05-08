from django.urls import path
from .views import BookDetailView, BookListView

books_patterns = ([
    path('', BookListView.as_view(), name='books'),
], 'books')