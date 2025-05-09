from django.urls import path
from .views import BookDetailView, BookListView, BookCreateView

books_patterns = ([
    path('', BookListView.as_view(), name='books'),
    path('<int:pk>/<slug:slug>', BookDetailView.as_view(), name='book'),
    path('create/', BookCreateView.as_view(), name='create')
], 'books')