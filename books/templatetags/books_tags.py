from django import template
from books.models import Genre

register = template.Library()

@register.simple_tag()
def categories():
    return Genre.objects.all()
