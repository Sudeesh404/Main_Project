from django.db import models
from myapp.models import *
from Admin.models import *

# Create your models here.
class Ins(models.Model):
    password = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    station_name = models.CharField(max_length=30, null=False, unique=True, default="none")
    station_id = models.CharField(max_length=10, unique=True, default="1")
    address = models.CharField(max_length=100, default="none")
    phone = models.CharField(max_length=15, default="0000000")
    pic = models.FileField(upload_to='Profile', default='default.jpg')

    def __str__(self):
        return self.station_name


class Sub(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone=models.CharField(max_length=10)
    pic = models.FileField(upload_to = 'Profile', default='default.jpg')

    def __str__(self):
        return self.fname + " " + self.lname
    



class MostWanted(models.Model):
    full_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    height = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    eye_color = models.CharField(max_length=50)
    hair_color = models.CharField(max_length=50)
    distinguishing_features = models.TextField()
    offenses_committed = models.TextField()
    last_known_location = models.CharField(max_length=100)
    rewards_offered = models.CharField(max_length=100, blank=True)
    recent_photographs = models.ImageField(upload_to='most_wanted_photos/')
    contact_numbers = models.CharField(max_length=100)
    background_information = models.TextField(blank=True)
    known_addresses = models.TextField(blank=True)
    date_of_last_known_activity = models.DateField(blank=True, null=True)
    current_status = models.CharField(max_length=50)
    

    def __str__(self):
        return self.full_name
