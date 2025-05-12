from django.db import models
from django.core.validators import validate_image_file_extension
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    """  Modelo de Libro con titulo, autor, sinopsis y creación """
    title = models.CharField(verbose_name='Título', max_length=100)
    author = models.CharField(verbose_name='Autor', max_length=100)
    sinopsis = models.TextField(verbose_name='Sinopsis', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    image = models.ImageField(verbose_name='Portada', upload_to='books/', null=True, blank=True, validators=[validate_image_file_extension])
    genres = models.ManyToManyField(Genre, verbose_name='Género', related_name='get_books', null=True, blank=True)
    owned = models.ManyToManyField(User, verbose_name='Pertenece', related_name='maps')

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['title']

    def __str__(self):
        return self.title