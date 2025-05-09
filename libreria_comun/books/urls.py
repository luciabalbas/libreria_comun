from django.urls import path
from .views import BookDetailView, BookListView

books_patterns = ([
    path('', BookListView.as_view(), name='books'),
    path('<int:pk>/<slug:slug>', BookDetailView.as_view(), name='book')
], 'books')