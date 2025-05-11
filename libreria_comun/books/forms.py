from django import forms
from .models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    """ Formulario que posee el modelo Book """
    class Meta:
        model = Book
        fields = ['title', 'author', 'sinopsis', 'image']
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
        }
        labels = {
            'title': '', 'author': '', 'sinopsis': '',
        }