from django.db import models
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Государство', unique=True)

    class Meta:
        db_table = "country"
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class Author(models.Model):
    name_author = models.CharField(max_length=100, verbose_name='Автор', db_index=True)
    birthday = models.DateTimeField(auto_now_add=True, verbose_name="Дата рождение")
    country = models.ManyToManyField(Country, verbose_name="Страна")
    biography = models.TextField(verbose_name='биография', blank=True)
    image = models.ImageField(verbose_name=' фото', upload_to='books', blank=True)


    class Meta:
        db_table = "author"
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name_author


class Book(models.Model):
    name_book = models.CharField(max_length=100, verbose_name='Название книги',unique=True)
    image = models.ImageField(verbose_name=' фото', upload_to='books')
    author = models.ManyToManyField(Author, verbose_name='Автор', related_name='aut')
    quantity_page = models.PositiveSmallIntegerField(verbose_name='Количество страниц', blank=True)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, related_name='genre_id', verbose_name='жанр')
    date_publish = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    description = models.TextField(verbose_name='Описание', blank=True)
    country = models.ManyToManyField(Country, verbose_name="Страна")
    text_book = models.FileField(verbose_name='файл', blank=True, upload_to='file/')



    def __str__(self):
        return self.name_book

    class Meta:
        db_table = "book"
        default_permissions = ('add', 'change', 'view')
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'





class Genre(models.Model):
    genre = models.CharField(max_length=100, verbose_name='Жанр', unique=True, db_column='Жанр')
    description = models.TextField(verbose_name='Описание', db_column='Описание')
    image = models.ImageField(verbose_name='Фото', upload_to='genre', null=True)
    slug = models.SlugField(max_length=50, verbose_name='Слаг', unique=True, db_index=True)

    class Meta:
        db_table = "genre"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


    def __str__(self):
        return self.genre


