from django import template
import datetime
from django.db import connection
from collections import namedtuple

register = template.Library()

@register.filter
def get_full_gender(obj):
    if obj == 'M':
        return "Male"
    elif obj == 'F':
        return "Female"
    else:
        return "Others/Not Specified"