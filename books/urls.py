from django.urls import path
from .views import (MainListView,
                    GenreListView,
                    GenerDetailView,
                    AddBooksView,
                    RegisterUserView,
                    LoginUserView )

app_name = 'books'

urlpatterns = [
    path("", MainListView.as_view(), name='home'),
    path('genre/<int:pk>/', GenerDetailView.as_view(), name='genre_cat'),
    path('add/', AddBooksView.as_view(), name='add_books'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),

]