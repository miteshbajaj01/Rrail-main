from django import template
from ..models import *
import datetime
from django.db import connection
from collections import namedtuple

register = template.Library()

cursor = connection.cursor()

def namedtuplefetchall(cursor):
    desc = cursor.description
    result = namedtuple('Result', [col[0] for col in desc])
    return [result(*row) for row in cursor.fetchall()]


@register.filter
def count(obj):
    return len(obj)

@register.filter
def get_delay(obj):
    departure = datetime.datetime.combine(datetime.date.today(), obj.departure)
    arrival = datetime.datetime.combine(datetime.date.today(), obj.arrival)
    if obj.arrival > obj.departure:
        departure = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), obj.departure)
    delay = departure - arrival
    return f'{delay.seconds//3600}:{(delay.seconds//60)%60}'

@register.filter
def get_travel_time(obj):
    source_time = datetime.datetime.combine(datetime.date.today(), obj['source'][0])
    day_diff = obj['destination'][1] - obj['source'][1]
    destination_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=day_diff), obj['destination'][0])
    delay = destination_time - source_time
    return f'{delay.seconds//3600}:{(delay.seconds//60)%60}'


@register.filter
def split(obj):
    return obj.split(' ')

@register.filter
def get_full_station_name(obj):
    cursor.execute(f"SELECT `station_name` FROM `website_station` WHERE `station_code` = '{obj}'")
    station_name = cursor.fetchone()[0]

    return station_name

@register.filter
def get_full_train_name(obj):
    cursor.execute(f"SELECT `train_name` FROM `website_train` WHERE `train_no` = '{obj}'")
    station_name = cursor.fetchone()[0]

    return station_name

@register.filter
def get_full_gender(obj):
    if obj == 'M':
        return "Male"
    elif obj == 'F':
        return "Female"
    else:
        return "Others/Not Specified"