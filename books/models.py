from django.core.validators import MaxValueValidator
from django.db import models

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

    class Meta:
        db_table = "genre"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


    def __str__(self):
        return self.genre




class Publisher(models.Model):
    name_publisher = models.CharField(max_length=100, verbose_name='Название издательства')
    address = models.TextField(verbose_name='Адрес',)
    phone = models.CharField(max_length=100, verbose_name='Телефон', unique=True)

    class Meta:
        db_table = "publisher"
        verbose_name = 'издательства'
        verbose_name_plural = 'издательства'

    def __str__(self):
        return self.name_publisher




class Reader(models.Model):
    name_user = models.CharField( verbose_name='имя читатель', max_length=100)
    email = models.EmailField( verbose_name='электронная почта', max_length=100, blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='возрост ', validators=[MaxValueValidator(150)], blank=True)


    class Meta:
        db_table = "reader"
        verbose_name = 'читатель'
        verbose_name_plural = 'читатели'

    def __str__(self):
        return self.name_user


















# quality = (
#     ('not', 'не известно'),
#     ('HDRip', 'HDRip'),
#     ('HDTVRip', 'HDTVRip'),
#     ('WEB - DLRip', 'WEB - DLRip'),
#     ('HD DVDRip', 'HD DVDRip'),
#     ('BDRip', 'BDRip'),
# )
#
#
# class Country(models.Model):
#     name = models.CharField(verbose_name='название', max_length=100)
#
#     class Meta:
#         verbose_name =  'Страна'
#         verbose_name_plural = 'Страна'
#
#     def __str__(self):
#         return self.name
#
#
#
#
# class Films(models.Model):
#     name = models.CharField(verbose_name='название', max_length=100)
#     age = models.DateField(verbose_name='дата выхода', max_length=100)
#     description = models.TextField(verbose_name='описание', blank=True)
#     image = models.ImageField(verbose_name=' фото', upload_to='d')
#     quality = models.CharField(verbose_name='качесто',max_length=100, choices=quality, default='not' )
#     country = models.ForeignKey(Country, on_delete=models.SET_NULL,verbose_name='страна', related_name='films_country', null=True)
#     gener = models.ForeignKey('Genre', on_delete=models.SET_NULL, verbose_name='жанр', related_name='films_gener',  null=True)
#
#     class Meta:
#         verbose_name = 'Фильм'
#         verbose_name_plural = 'Филмы'
#
#     def __str__(self):
#         return self.name
#
#
# class Genre(models.Model):
#     name = models.CharField(verbose_name='название', max_length=100)
#     description = models.TextField(verbose_name='описание', blank=True)
#
#     class Meta:
#         verbose_name = 'Жанр'
#         verbose_name_plural = 'Жанры'
#
#
#     def __str__(self):
#         return self.name
