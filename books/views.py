from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from .models import Book, Genre
from .forms import AddBooksForm, RegisterUserForm



class MainListView(ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'books'




class GenreListView(ListView):
    model = Genre
    template_name = 'books/genre.html'
    context_object_name = 'genres'



class GenerDetailView(DetailView):
    model = Genre
    template_name = 'books/detail.html'
    context_object_name = 'gener'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['GG'] = Book.objects.all()
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
    form_class = AuthenticationForm
    template_name = 'books/login.html'
    success_url = reverse_lazy('books:add_books')


