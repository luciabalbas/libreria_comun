from django.contrib import admin
from .models import Book, Genre

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    ordering = ('title',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    ordering = ('name',)

admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)