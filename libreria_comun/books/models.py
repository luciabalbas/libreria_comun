from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Book(models.Model):
    """  Modelo de Libro con titulo, autor, sinopsis y creación """
    title = models.CharField(verbose_name='Título', max_length=100)
    author = models.CharField(verbose_name='Autor', max_length=100)
    sinopsis = models.TextField(verbose_name='Sinopsis', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    image = models.ImageField(verbose_name='Portada', upload_to='books/', null=True, blank=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['title']

    def __str__(self):
        return self.title