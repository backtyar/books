from django import forms

from .models import Book

class AddBooksForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            'name_book', 'author', 'quantity_page', 'genre',
            'description', 'country', 'image', 'text_book'
        ]

