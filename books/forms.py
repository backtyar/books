from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


from .models import Book

class AddBooksForm(forms.ModelForm):

    class Meta:
        model = Book

        fields = [
            'name_book', 'description', 'genre', 'author',
            'country', 'quantity_page', 'image', 'text_book'
        ]

        widgets = {
            "name_book": forms.TextInput(attrs={"class": "firstname", 'placeholder': "Называние книги.."}),
            "author": forms.CheckboxSelectMultiple(attrs={"class": "firstname", 'placeholder': "Автор.."}),
            "description": forms.Textarea(attrs={"class": "firstname", 'placeholder': "Описание..",  "id":"fname"}),
            "image": forms.FileInput(attrs={"class": "firstname", 'placeholder': "Фото.."}),
            "country": forms.CheckboxSelectMultiple(attrs={"class": "firstname", "id":"country"}),
            "genre": forms.Select(attrs={"class": "firstname"}),
            "quantity_page": forms.NumberInput(attrs={}),
            "text_book": forms.FileInput(attrs={"class": "firstname", 'placeholder': "Файл книги.."})
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Имя пользователя.."}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": "Пароль",}))
    password2 = forms.CharField(label='Потвердить Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": "Потвердить пароль",}))


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')






class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={"input type": 'text', "id": 'inputEmail', "class": "form-control", "name": "username", "placeholder": "логин", "maxlength": "150", "required": ""}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control", "id": "inputPassword", "placeholder": "Пароль", "name": "username", "placeholder": "Пароль", "maxlength": "150", "required": ""}))


    class Meta:
        model = User
        fields = ('username', 'password1')








