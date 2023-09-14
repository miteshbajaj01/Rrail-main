from django.db import models
from accounts.models import *

CLASS_CHOICES=(
    ('1A', '1A'),
    ('2A', '2A'),
    ('3A', '3A'),
    ('SL', 'SL'),
)


class demo(models.Model):
    id=models.CharField(max_length=10, primary_key=True)
    name=models.CharField(max_length=30)
    def __str__(self):
        return f'{self.id} {self.name}'
        
class Station(models.Model):
    station_code = models.CharField(max_length=10, primary_key=True)
    station_name = models.CharField(max_length=30)
    station_master = models.CharField(max_length=20, default='')

    def __str__(self):
        return f'{self.station_name} ({self.station_code})'


class Train(models.Model):
    train_no = models.CharField(max_length=5, primary_key=True)
    train_name = models.CharField(max_length=100)
    run_days = models.CharField(max_length=100)
    source = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='train_source')
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='train_destination')

    def __str__(self):
        return f'{self.train_no} - {self.train_name}'


class TrainSchedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    arrival = models.TimeField()
    departure = models.TimeField()
    distance = models.IntegerField()
    day = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.train} at {self.station}'


class Booking(models.Model):
    pnr = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=20)
    train_no = models.ForeignKey(Train, max_length=5, on_delete=models.CASCADE)
    journey_date = models.CharField(max_length=10)
    seats = models.IntegerField()
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.pnr} by {self.booked_by}'

class Seats(models.Model):
    train=models.ForeignKey(Train, on_delete=models.CASCADE)
    date = models.CharField(max_length=10)
    seats = models.IntegerField()


