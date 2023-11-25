from django.contrib import admin
from .models import Book, Author, Publisher, Genre, Reader ,Country

@admin.register(Country)
class AdminCountry(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']



@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ['id', 'name_book','quantity_page','genre', 'date_publish', 'description', 'image',]
    list_display_links = ['name_book']
    search_fields = ['name_book']


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ['id', 'name_author', 'birthday',        'image']
    list_display_links = ['name_author']
    search_fields = ['name_author']


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ['id', 'genre', 'description']
    list_display_links = ['genre']
    search_fields = ['genre']


@admin.register(Publisher)
class AdminPublisher(admin.ModelAdmin):
    list_display = ['id', 'name_publisher', 'address', 'phone']
    list_display_links = ['name_publisher']
    search_fields = ['name_publisher']


@admin.register(Reader)
class AdminReader(admin.ModelAdmin):
    list_display = ['id', 'name_user','email', 'age']
    list_display_links = ['name_user']
    search_fields = ['name_user']
