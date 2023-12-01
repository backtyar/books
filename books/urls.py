from django.urls import path
from .views import MainListView, GenreListView, GenerDetailView, AddBooksView

app_name = 'books'

urlpatterns = [
    path("", MainListView.as_view(), name='home'),
    path('genre/<int:pk>/', GenerDetailView.as_view(), name='genre_cat'),
    path('add/', AddBooksView.as_view(), name='add_books')

]