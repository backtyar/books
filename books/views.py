from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from .models import Book, Genre
from .forms import AddBooksForm, RegisterUserForm, LoginUserForm

class MainListView(ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'books'


class GenreListView(ListView):
    model = Genre
    template_name = 'books/genre.html'
    context_object_name = 'genres'


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'books/genre_detail.html'
    context_object_name = 'genre'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(genre=self.object.pk)
        return context


class AddBooksView(CreateView):
    form_class = AddBooksForm
    template_name = 'books/add_books.html'
    success_url = reverse_lazy('books:home')


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'books/register.html'
    success_url = reverse_lazy('books:home')



class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'books/login.html'

    def get_success_url(self):
        return reverse_lazy('books:add_books')


