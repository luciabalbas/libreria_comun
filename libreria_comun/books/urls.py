from django.urls import path
from .views import BookDetailView, BookListView, BookCreateView, BookUpdate, BookDelete, GenreList
from . import views

books_patterns = ([
    path('', BookListView.as_view(), name='books'),
    path('<int:pk>/<slug:slug>', BookDetailView.as_view(), name='book'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('update/<int:pk>', BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>', BookDelete.as_view(), name='delete'),
    path('search/', views.search_book, name='search'),
    path('genre/<int:genre_id>', GenreList.as_view(), name='genre'),
], 'books')