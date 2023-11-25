from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Genre

app_name = 'books'
class MainListView(ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'books'


class GenreListView(ListView):
    model = Genre
    template_name = 'books/genre.html'
    context_object_name = 'genres'


