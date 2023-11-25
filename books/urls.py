from django.urls import path
from .views import MainListView, GenreListView

app_name = 'books'

urlpatterns = [
    path("", MainListView.as_view(), name='home'),
    path('gener/', GenreListView.as_view(), name='genre')
]