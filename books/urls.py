from django.urls import path
from .views import (MainListView,
                    GenreListView,
                    AddBooksView,
                    RegisterUserView,
                    LoginUserView,
                    GenreDetailView)

app_name = 'books'

urlpatterns = [
    path("", MainListView.as_view(), name='home'),
    path('genre/', GenreListView.as_view(), name='genre_cat'),
    path('gener/<slug:slug>/', GenreDetailView.as_view(), name='genre_detail'),
    path('add/', AddBooksView.as_view(), name='add_books'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),

]