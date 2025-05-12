from django import forms
from .models import Book, Genre
from django.contrib.auth.models import User
class BookForm(forms.ModelForm):
    """ Formulario que posee el modelo Book """
    class Meta:
        model = Book
        fields = ['title', 'author', 'sinopsis', 'genres', 'owned', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
               'class':  'form-control p-3',
               'placeholder': 'Titulo',
            }),
            'author': forms.TextInput(attrs={
               'class':  'form-control p-3',
               'placeholder': 'Autor',
            }),
            'sinopsis': forms.Textarea(attrs={
               'class':  'form-control p-3',
               'placeholder': 'Sinopsis',
            }),
            'genres': forms.SelectMultiple(attrs={
                'class': 'form-select',
            }, choices = Genre.objects.all()
            ),
            'owned': forms.SelectMultiple(attrs={
                'class': 'form-select',
            }, choices=User.objects.all()
            ), 
        }
        labels = {
            'title': '', 'author': '', 'sinopsis': '', 'genres': '', 'owned': '',
        }