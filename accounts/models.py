from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER_CHOICES=(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others/Not Specified'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.user.username