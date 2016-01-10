from django import template
from django.template.defaulttags import register

register = template.Library()

"""
   Template filter for getting item variable lookup.
"""
@register.filter
def get_item(dictionary, key):
    return dictionary[key]
